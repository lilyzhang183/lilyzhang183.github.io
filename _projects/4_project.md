---
layout: page
title: Cozy Home
description: >
  ODE indoor-climate model with Fourier heat loss and window air
  exchange; device effects via sparse M1, M2 on binary Y; quadratic discomfort
  with PD S_i; derived c_opt = (Σ S_i)^(-1) Σ S_i c_{p,i} and S_eff = Σ S_i.
  Time-weighted least squares (daily/weekly/annual kernels) to estimate c_opt(t),
  S_eff(t), and conductivity σ; thresholded control rule for device switching.
img:
importance: 3
category: fun
---

### Overview

- ODE indoor-climate model with Fourier heat loss and window air exchange.  
- Device effects via sparse matrices $M_1$, $M_2$ acting on binary state $Y$.  
- Quadratic discomfort with positive-definite $S_i$; derived:  
  - $c_{\mathrm{opt}}=(\sum_i S_i)^{-1}\sum_i S_i c_{p,i}$  
  - $S_{\mathrm{eff}}=\sum_i S_i$
- Time-weighted least squares (daily/weekly/annual kernels) to estimate
  $c_{\mathrm{opt}}(t)$, $S_{\mathrm{eff}}(t)$, and conductivity $\sigma$.  
- Implemented a thresholded control rule for device switching.

<p class="mt-3 mb-2">
  <a class="btn btn-sm btn-outline-primary"
     href="{{ '/assets/432.pdf' | relative_url }}"
     target="_blank" rel="noopener">
    View PDF
  </a>
  <a class="btn btn-sm btn-outline-secondary"
     href="{{ '/assets/432.pdf' | relative_url }}"
     download>
    Download
  </a>
</p>

<!-- Embedded PDF (falls back to the links above if the browser can't embed PDFs) -->
<object data="{{ '/assets/432.pdf' | relative_url }}"
        type="application/pdf" width="100%" style="height:70vh">
  <p>
    PDF viewer unavailable.
    <a href="{{ '/assets/432.pdf' | relative_url }}">Open the PDF</a>.
  </p>
</object>
