"""LaTeX -> typst -> PDF via pandoc + typst, for environments without a TeX installation.

Usage:  pip install pypandoc_binary typst
        python3 build_pdf.py dimension-cost.tex dimension-cost.pdf

The real source is the .tex file; this script only produces a readable preview.  Known
differences from a pdflatex build: theorem environments are numbered sequentially (pandoc does
not honour the [section] option), and the appendix is numbered as an ordinary section.
"""
import os
import re
import sys

import pypandoc
import typst


def matching_bracket(s, i):
    """s[i] == '['; return the index of the matching ']' (skips escaped brackets)."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def preprocess_tex(src):
    """Replace thebibliography/\\cite by plain text so that pandoc and typst can handle them."""
    labels = dict(re.findall(r'\\bibitem\[([^\]]*)\]\{([^}]*)\}', src))
    key2lab = {k: l for l, k in labels.items()}

    def cite(m):
        keys = [k.strip() for k in m.group(1).split(',')]
        return '{[' + ', '.join(key2lab.get(k, k) for k in keys) + ']}'

    src = re.sub(r'\\cite\{([^}]*)\}', cite, src)
    src = src.replace('\\begin{thebibliography}{99}', '\\section*{References}\n\\begin{itemize}')
    src = src.replace('\\end{thebibliography}', '\\end{itemize}')
    src = re.sub(r'\\bibitem\[([^\]]*)\]\{[^}]*\}', r'\\item {[\1]}', src)
    src = src.replace('\\appendix', '')
    return src


DELIM = {'chevron.l': '⟨', 'chevron.r': '⟩', 'parallel': '‖', 'bar.v.double': '‖', 'bar.v': '|',
         '\\(': '(', '\\)': ')', '\\[': '[', '\\]': ']', '\\{': '{', '\\}': '}',
         'floor.l': '⌊', 'floor.r': '⌋', 'ceil.l': '⌈', 'ceil.r': '⌉'}


def postprocess_typ(s):
    # 1. theorem-like blocks "#block[ #strong[Name N] ... ] <label>": label -> number
    numbers = {}
    pos = 0
    while True:
        i = s.find('#block[', pos)
        if i < 0:
            break
        j = matching_bracket(s, i + 6)
        if j < 0:
            break
        m = re.match(r'\s*<([^>]+)>', s[j + 1:])
        if m:
            mm = re.search(r'#(?:strong|emph)\[[A-Z][A-Za-z]+ ([0-9.]+)', s[i + 7:j])
            if mm:
                numbers[m.group(1)] = mm.group(1)
            else:
                numbers[m.group(1)] = '[?]'
                print('WARNING: unnumbered block label', m.group(1))
        pos = i + 7

    # 2. normalise every "@label" (typst would swallow trailing punctuation) to "#ref(<label>)"
    def fix_ref(m):
        lab = m.group(1).rstrip(':.-')
        rest = m.group(1)[len(lab):]
        return '#ref(<%s>)%s' % (lab, rest)
    s = re.sub(r'@([A-Za-z0-9:_-]+)', fix_ref, s)

    # 3. references to theorem-like blocks -> their numbers
    for lab, num in numbers.items():
        s = s.replace('#ref(<' + lab + '>)', num)
        s = re.sub(r'#link\(<' + re.escape(lab) + r'>\)\[[^\]]*\]', num, s)

    # 4. equation references -> "(n)"; typst numbers every display equation "$ ... $" in order
    eqnums = {}
    dollars = [m.start() for m in re.finditer(r'(?<!\\)\$', s)]
    count = 0
    for a, b in zip(dollars[0::2], dollars[1::2]):          # pair opening/closing dollars in order
        inner = s[a + 1:b]
        if inner.startswith(' ') and inner.endswith(' '):    # pandoc writes display math as "$ ... $"
            count += 1
            m = re.match(r'<([^>]+)>', s[b + 1:])
            if m:
                eqnums[m.group(1)] = str(count)

    def eqref(m):
        lab = m.group(1)
        return '(' + eqnums[lab] + ')' if lab in eqnums else '#ref(<' + lab + '>)'
    s = re.sub(r'#link\(<([^>]+)>\)\[\\\[[^\]]*\\\]\]', eqref, s)
    s = re.sub(r'#ref\(<(eq:[A-Za-z0-9_-]+)>\)', lambda m: '(' + eqnums.get(m.group(1), '?') + ')', s)

    # 5. remaining refs point to headings: the text already says "Section", so no supplement
    s = re.sub(r'#ref\(<([^>]+)>\)', r'#ref(<\1>, supplement: none)', s)

    # 6. pandoc's scaled delimiters "#scale(...)[sym]" -> plain unicode delimiters
    s = re.sub(r'#scale\(x: \d+%, y: \d+%\)\[([^\]]*)\]', lambda m: DELIM.get(m.group(1), m.group(1)), s)

    # 7. symbol names pandoc emits that this typst version does not know
    for bad, good in [(' wreath ', ' ≀ '), ('times.circle', '⊗'), ('plus.circle', '⊕'), ('lt.tri.eq', '⊴')]:
        s = s.replace(bad, good)

    # 8. number display equations
    s = s.replace('#show: doc => conf(', '#set math.equation(numbering: "(1)")\n#show: doc => conf(', 1)
    return s, numbers


def build(tex, out_pdf):
    base = os.path.splitext(tex)[0]
    tmp_tex = base + '.pandoc.tex'
    open(tmp_tex, 'w').write(preprocess_tex(open(tex).read()))
    typ = base + '.typ'
    pypandoc.convert_file(tmp_tex, 'typst', outputfile=typ,
                          extra_args=['--standalone', '--number-sections', '--toc', '--wrap=none'])
    s, numbers = postprocess_typ(open(typ).read())
    open(typ, 'w').write(s)
    typst.compile(typ, output=out_pdf)
    os.remove(tmp_tex)
    return numbers


if __name__ == '__main__':
    numbers = build(sys.argv[1], sys.argv[2])
    print('theorem labels resolved:', len(numbers), '; pdf bytes:', os.path.getsize(sys.argv[2]))
