// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-research",
          title: "research",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "nav-service",
          title: "service",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/service/";
          },
        },{id: "post-google-gemini-updates-flash-1-5-gemma-2-and-project-astra",
        
          title: 'Google Gemini updates: Flash 1.5, Gemma 2 and Project Astra <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "We’re sharing updates across our Gemini family of models and a glimpse of Project Astra, our vision for the future of AI assistants.",
        section: "Posts",
        handler: () => {
          
            window.open("https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/", "_blank");
          
        },
      },{id: "post-displaying-external-posts-on-your-al-folio-blog",
        
          title: 'Displaying External Posts on Your al-folio Blog <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.open("https://medium.com/@al-folio/displaying-external-posts-on-your-al-folio-blog-b60a1d241a0a?source=rss-17feae71c3c4------2", "_blank");
          
        },
      },{id: "news-a-simple-inline-announcement",
          title: 'A simple inline announcement.',
          description: "",
          section: "News",},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-a-simple-inline-announcement-with-markdown-emoji-sparkles-smile",
          title: 'A simple inline announcement with Markdown emoji! :sparkles: :smile:',
          description: "",
          section: "News",},{id: "projects-baire-category-theorem-and-its-applications",
          title: 'Baire Category Theorem and Its Applications',
          description: "Exposition of the Baire Category Theorem (equivalent formulations) with applications to the Uniform Boundedness Principle and the Closed Graph Theorem; worked examples include a generic-but-measure-zero set and Grothendieck’s theorem (closed subspaces of L^p contained in L^\infty on finite-measure spaces are finite-dimensional).",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-real-analysis-notes",
          title: 'Real Analysis Notes',
          description: "Notes from my first college math course (Fall 2019). Typeset with my self-designed LaTeX template.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-cozy-home",
          title: 'Cozy Home',
          description: "ODE indoor-climate model with Fourier heat loss and window air exchange; device effects via sparse M1, M2 on binary Y; quadratic discomfort with SPD S_i; derived c_opt = (Σ S_i)^(-1) Σ S_i c_{pi} and S_eff = Σ S_i. Time-weighted least squares (daily/weekly/annual kernels) to estimate c_opt(t) and the exchange-rate matrix σ; S_eff configured (SPD). Implemented a thresholded control rule for device switching.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-understanding-housing-bubble-in-vancouver-bc",
          title: 'Understanding Housing Bubble in Vancouver, BC',
          description: "Δlog HPI (2005–2021): ADF; SARIMA (2,1,0)×(2,0,0)_12 via AIC/BIC; Ljung–Box; 12-month forecasts. VAR(1) on first differences of HPI, GDP, 10-yr yield, CAD/USD, employment, earnings, CPI, crime + Bill-28 dummy; Granger, Cholesky IRFs, FEVD. Results: HPI variance mostly self-driven; GDP predictive (95%); employment marginal (90%); CPI/yield short-run; policy coefficient negative/significant.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-an-algorithmic-approach-to-knapsack-problems",
          title: 'An Algorithmic Approach to Knapsack Problems',
          description: "Survey of 0-1, fractional, and multi-dimensional knapsack; implementations of dynamic programming, a scaling FPTAS, and a 1/2-approximate greedy (fractional greedy proved optimal). Python benchmarks for MDKP and baselines; GA and local- search heuristics explored.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-understanding-burnside-39-s-theorem",
          title: 'Understanding Burnside&amp;#39;s Theorem',
          description: "Expository, character-theoretic proof of Burnside&#39;s p^a q^b solvability theorem via Sylow theory, the class equation, column orthogonality, and algebraic-integer methods; key lemmas (|χ(g)| ≤ χ(1), conjugacy-class size criterion).",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%79%6F%75@%65%78%61%6D%70%6C%65.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-inspire',
        title: 'Inspire HEP',
        section: 'Socials',
        handler: () => {
          window.open("https://inspirehep.net/authors/1010907", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qc6CJjYAAAAJ", "_blank");
        },
      },{
        id: 'social-custom_social',
        title: 'Custom_social',
        section: 'Socials',
        handler: () => {
          window.open("https://www.alberteinstein.com/", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
