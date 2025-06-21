---
marp: true
title: Python in the Browser
author: Anand S
url: https://sanand0.github.io/talks/2025-06-pycon-sg
theme: gaia
backgroundColor: white
paginate: true
# Build: npx -y @marp-team/marp-cli@latest README.md -o index.html
---

<!-- _backgroundColor: #defa9d -->
<style>figure { margin-right: 1rem !important; }</style>

# Python in the Browser

### [Anand S](https://s-anand.net/)

###### LLM Psychologist @ Straive

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-pycon-sg/)

Slides: [sanand0.github.io/talks/2025-06-pycon-sg/](https://sanand0.github.io/talks/2025-06-pycon-sg/)

---

## Hypothesis Forge: Automating Analysis

- [Hypoforge: sanand0.github.io/hypoforge/](https://sanand0.github.io/hypoforge/)
- **One-click insights** over _any_ CSV right in the browser-no backend, no install
- Uses Pyodide + Web Worker to run pandas & SciPy in the browser
- Perfect for classrooms, hackathons, client demos. Just share a URL

---

## Anatomy of the Magic

After the LLM generates code, here's how we run it.

```html
<script src="https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js"></script>
<script>
  const pyodide = await loadPyodide();
  await pyodide.loadPackage(['pandas', 'numpy']);
  const df = pyodide.runPython(`
      import pandas as pd, io, base64, sys
      csv = "sepal_length,sepal_width\\n5.1,3.5"
      pd.read_csv(io.StringIO(csv)).describe().to_string()
  `);
  console.log(df);
</script>
```

---

## How it Works

- **`loadPyodide()`** fetches the 6 MB WASM; cache-able.
- `await pyodide.loadPackage('scikit-learn')` lazy-installs wheels from PyPI mirror; tiny overlays.
- **`runPython()`** executes & transparently converts basic types :left_right_arrow: JS

**Python-in-browser is production-ready today.**

---

## Common Pitfalls (and Fixes)

- **UI freezes on first load**. Move everything into the worker before `loadPyodide()`
- **"Module not found" wheels**. Pin exact package version; manylibs lag a bit
- **Memory bloat**. Call `pyodide.runPython('import gc; gc.collect()')` between large runs
- **CORS errors hosting locally**. Serve with `--cors` flag or a tiny Express proxy

---

# Use Python in the Browser

### [Anand S](https://s-anand.net/)

###### LLM Psychologist @ Straive

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-06-pycon-sg/)

Slides: [sanand0.github.io/talks/2025-06-pycon-sg/](https://sanand0.github.io/talks/2025-06-pycon-sg/)
