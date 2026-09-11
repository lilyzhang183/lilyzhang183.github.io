window.MathJax = {
  tex: {
    tags: "ams",
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
  },
  output: {
    // AMS Euler (Neo Euler) letters, digits, Greek, \mathcal, \mathfrak and big operators,
    // layered on MathJax's default font, which supplies everything Euler lacks.
    fontExtensions: ["mathjax-euler"],
  },
  chtml: {
    // Keep math at its natural size: Euler's x-height already matches the Palatino text,
    // and MathJax measures the surrounding font only once, possibly before it has loaded.
    matchFontHeight: false,
  },
  loader: {
    // The Euler extension 4.1.3 still declares version 4.0.0, which only causes a console warning.
    versionWarnings: false,
  },
  startup: {
    ready() {
      MathJax.startup.defaultReady();
      // Work around a MathJax 4.1.3 bug: fonts added by the Euler extension's dynamic ranges
      // (\mathfrak and bold Greek) are requested from the base font's folder and fail to load.
      // Point them at the extension's own woff2 folder. If this ever fails, math still renders.
      try {
        const font = MathJax.startup.document.outputJax.font;
        const eulerURL = MathJax._.components.package.Package.resolvePath("[mathjax-euler-extension]/chtml/woff2", false);
        const addCss = font.addDynamicFontCss.bind(font);
        font.addDynamicFontCss = (fonts, root) => addCss(fonts, fonts.some((f) => f.startsWith("MJX-NE-")) ? eulerURL : root);
      } catch (e) {}
    },
  },
  options: {
    // Keep assistive MathML for screen readers, as in MathJax 3, and don't start MathJax 4's speech worker.
    menuOptions: {
      settings: {
        speech: false,
        braille: false,
        assistiveMml: true,
      },
    },
    renderActions: {
      addCss: [
        200,
        function (doc) {
          const style = document.createElement("style");
          style.innerHTML = `
          .mjx-container {
            color: inherit;
          }
        `;
          document.head.appendChild(style);
        },
        "",
      ],
    },
  },
};
