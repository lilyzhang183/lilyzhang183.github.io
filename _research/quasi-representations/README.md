# Dimension cost of cancelling topological obstructions in quasi-representations of Z wr Z

Working materials for the research question on the nine-block family
`rho_n : Z wr Z -> U(9n^2)` (sharp dimension cost of a correction, the winding-number lower
bound lemma, the degree-four problem for `rho_n (+) conj(rho_n)`, and the further directions).

This folder starts with an underscore, so Jekyll ignores it: nothing here is published on the
website unless it is deliberately moved to `assets/` and linked from a page.

## Files

| File | What it is |
|---|---|
| `dimension-cost.tex` | The research note (LaTeX source, `amsart`). This is the primary deliverable. |
| `dimension-cost.pdf` | A rendering of the note produced **without LaTeX**, by `pandoc -> typst`. Theorem numbering is sequential (pandoc does not honour `[section]` numbering), otherwise the content is the same. Compile the `.tex` with `pdflatex` for the real thing. |
| `numerics.py` | Numerical verification (numpy/scipy): winding numbers, the sharp bound `|w| <= (m/pi) arcsin(delta/2)`, the explicit U-turn correction `(U_n (+) U_k, V_n (+) V_k^*) ~ commuting pair` with error `~ 3.5 k^{-1/2}`, and the polar-compression lemma on the output. |
| `numerics_output.txt` | Output of `python3 numerics.py` (the tables quoted in the appendix of the note). |
| `build_pdf.py` | The `pandoc -> typst` build used for the PDF (`pip install pypandoc_binary typst`, then `python3 build_pdf.py dimension-cost.tex dimension-cost.pdf`). |

## Status of the mathematics (see the summary at the top of the note)

* Proved: the quantitative winding-number bound, the polar-compression lemma, the lower bound
  `n' >= (2/3) |w| eta^{-2}` and `n' >= 4 |w| / eps_0`, the explicit correction with a complement of
  dimension `k <= n` and error `<= 13 k^{-1/2}`, the two-sided bound for Voiculescu pairs, and the
  wreath-product statement `n' ~ n max{eta^{-2}, eps_0^{-1}}` for the model family, including the
  negligible-overhead corollary and the limit `eta sqrt(n) -> infinity` for such corrections.
* Conditional: the degree-four lower bound `max{eta^{-4}, eps_0^{-2}}`, uniform in `n`, modulo a
  quantitative Chern-Weil estimate for almost commuting 4-tuples (the compression step is proved).
* Open: whether the `n`-independent candidate complement `Q (x) conj(Q) (+) conj(Q) (x) Q` works
  (a two-dimensional Berg lemma is the missing step).

## Caveat

The handwritten construction of `rho_n` was not available when this was written. The note fixes an
explicit model family with all the quoted features (period nine, `D^9 = I`, dimension `9n^2`,
degree-two winding number of magnitude `n`, non-zero degree-four character); all theorems are stated
for general period-`p` block families so that the original lamp blocks can be substituted directly.

The literature check in Section 7 of the note was done under a network policy that blocked arxiv.org
and most publisher sites; only search-engine summaries were available, and the section lists exactly
which claims could and could not be verified.
