# Playing with PyScript

I'm trying to learn [PyScript](https://pyscript.net/). My first project is an [accessible](https://www.w3.org/WAI/fundamentals/accessibility-intro/) org chart. The org chart is deployed using GitHub pages. See the [org chart demo](https://benjiallen.github.io/pyscript-playground/org-chart.html).

The data used in the org chart is based on names and GitHub handles of [cpython contributors](https://github.com/python/cpython/graphs/contributors). The manager relationships are completely fictitious.

## Features of pyscript that are used in this project

This project has been a useful learning tool as it uses numerous features of pyscript, including:

- Use of packages, outside of the standard library, that do and don't ship with pyodide
  - Packages that ship with pyodide and are used in this project
    - bleach
    - jinja2
  - Other packages used in this project
    - thefuzz
- Using Jinja templates to build the UI
- Using pyodide APIs to search and modify the DOM e.g., `document.getElementById`, `document.querySelectorAll`
- Using a JavaScript object from within Python
- Adding event listeners to DOM elements using `pyodide.ffi.wrappers.add_event_listener`
- Using the python standard library in the web browser! OMG, how cool is that?
