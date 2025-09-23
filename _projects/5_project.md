---
layout: page
title: Understanding Housing Bubble in Vancouver, BC: A Time Series Analysis
description: >
Δlog HPI (2005–2021): ADF; SARIMA (2,1,0)×(2,0,0)12 via AIC/BIC; Ljung–Box; 12-month forecasts. VAR(1) on first differences of HPI, GDP, 10-yr yield, CAD/USD, employment, earnings, CPI, crime with Bill-28 dummy; Granger, Cholesky IRFs, FEVD. Results: HPI variance mostly self-driven; GDP predictive (95%); employment marginal (90%); CPI/yield shocks short-run; policy coefficient negative/significant.
img: assets/img/1.jpg
importance: 3
category: fun
---

### Overview

- **Univariate modeling (HPI growth, 2005–2021):**
  - ADF stationarity tests on $\Delta\log(\mathrm{HPI})$.
  - ACF/PACF-guided SARIMA $(2,1,0)\times(2,0,0)_{12}$ chosen by AIC/BIC.
  - Ljung–Box diagnostics; 12-month out-of-sample forecasts.
- **Multivariate dynamics (VAR(1) in first differences):**
  - Variables: HPI, GDP, 10-year yield, CAD/USD, employment, earnings, CPI, crime;
    exogenous Bill 28 policy dummy.
  - Granger causality, Cholesky IRFs, and FEVD.
  - Findings: HPI variance mostly self-driven; GDP predictive (95%); employment marginal (90%);
    CPI/yield shocks are short-run; policy coefficient negative and significant.

<p class="mt-3 mb-2">
  <a class="btn btn-sm btn-outline-primary"
     href="{{ '/assets/452.pdf' | relative_url }}"
     target="_blank" rel="noopener">
    View PDF
  </a>
  <a class="btn btn-sm btn-outline-secondary"
     href="{{ '/assets/452.pdf' | relative_url }}"
     download>
    Download
  </a>
</p>

<!-- Embedded PDF (falls back to the links above if the browser can't embed PDFs) -->
<object data="{{ '/assets/452.pdf' | relative_url }}"
        type="application/pdf" width="100%" style="height:70vh">
  <p>
    PDF viewer unavailable.
    <a href="{{ '/assets/452.pdf' | relative_url }}">Open the PDF</a>.
  </p>
</object>

