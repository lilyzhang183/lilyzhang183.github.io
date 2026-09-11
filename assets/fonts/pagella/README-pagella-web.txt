Pagella Web
===========

The four web fonts in this folder set the text of lilyzhang183.github.io:

  pagella-web-regular.woff
  pagella-web-italic.woff
  pagella-web-bold.woff
  pagella-web-bolditalic.woff

They are a modified version (a "Derived Work" in the sense of the LaTeX
Project Public License) of TeX Gyre Pagella 2.501 by the GUST e-foundry.

Source
------
texgyrepagella-regular.otf, texgyrepagella-italic.otf,
texgyrepagella-bold.otf and texgyrepagella-bolditalic.otf, version 2.501,
as distributed in TeX Live 2025
(texmf-dist/fonts/opentype/public/tex-gyre/).

Unmodified originals are available from:
  https://www.gust.org.pl/projects/e-foundry/tex-gyre/pagella
  https://ctan.org/pkg/tex-gyre

Changes
-------
All changes were made on 2026-09-11 with fontTools 4.62.1 (fontTools.subset
and fontTools.ttLib). The outlines, hinting and advance widths of the
retained glyphs are unchanged.

1. Subset to these Unicode ranges, keeping only characters the original
   fonts contain, plus the glyphs those characters reach through the
   retained features:
     U+0020-007E, U+00A0-00FF, U+0100-017F, U+0218-021B, U+0237,
     U+02BB-02BC, U+02C6-02C7, U+02C9, U+02D8-02DD, U+0300-0304,
     U+0306-0308, U+030A-030C, U+0326-0328, U+2000-206F, U+20AC,
     U+2122, U+2190-2193, U+2212, U+2215, U+FB00-FB04, U+FEFF, U+FFFD
   The resulting coverage (identical in all four fonts) is:
     U+0020-007E, U+00A0-0137, U+0139-0148, U+014A-0165, U+0168-017F, U+0218-021B, U+0237, U+02C6-02C7, U+02D8-02DD, U+0300-0304, U+0306-0308, U+030A-030C, U+0326-0328, U+2000-200D, U+2010-201A, U+201C-201E, U+2020-2022, U+2026, U+202F-2037, U+2039-203B, U+203D, U+203F-2040, U+2044-2046, U+2052, U+2054, U+2057, U+205F-2064, U+20AC, U+2122, U+2190-2193, U+2212, U+2215, U+FB00-FB04, U+FEFF
2. Kept the OpenType features ccmp, frac, kern, liga, locl, mark and mkmk.
   Removed the features aalt, c2sc, cpsp, dlig, lnum, onum, pnum, salt,
   size, smcp, ss01, ss02, ss03, ss04, ss10, tnum and zero, together with
   the glyphs used only by them. The .notdef glyph keeps its outline.
3. Removed the FFTM table (a FontForge timestamp).
4. Renamed the fonts, as the GUST Font License requests for derived works.
   Family name "Pagella Web"; PostScript names PagellaWeb-Regular,
   PagellaWeb-Italic, PagellaWeb-Bold and PagellaWeb-BoldItalic, set in both
   the name table and the CFF table (FontName, FamilyName, FullName). Name
   IDs 1-6 were rewritten accordingly; name IDs 16 and 17 (the typographic
   family and subfamily, which named the original font) were removed; and
   name IDs 10 (a description of these changes), 13 (license) and 14
   (license URL) were added.
5. Converted from OpenType (CFF) to WOFF 1.0.
6. As part of subsetting and saving, fontTools recalculated the values that
   depend on the glyph set: the OS/2 Unicode-range and code-page bits, the
   head bounding box and modification date, and the hhea extents.

Manifest
--------
  README-pagella-web.txt       this file
  GUST-FONT-LICENSE.txt        the license, as published by GUST
  pagella-web-regular.woff     derived from texgyrepagella-regular.otf
  pagella-web-italic.woff      derived from texgyrepagella-italic.otf
  pagella-web-bold.woff        derived from texgyrepagella-bold.otf
  pagella-web-bolditalic.woff  derived from texgyrepagella-bolditalic.otf

License
-------
The original copyright notice is kept in every font (name ID 0 and the CFF
Notice):

  Copyright 2006-2018 for TeX Gyre extensions by B. Jackowski,
  J.M. Nowacki, et al. (on behalf of TeX USERS GROUPS). Vietnamese
  characters were added by Han The Thanh.

These fonts are distributed under the GUST Font License
(GUST-FONT-LICENSE.txt), which is an instance of the LaTeX Project Public
License (LPPL), version 1.3c or later: https://www.latex-project.org/lppl.txt

This is a modified version. The GUST e-foundry and the authors of
TeX Gyre Pagella do not provide support for it. Please report problems with
these files to the maintainer of lilyzhang183.github.io, not to GUST.
