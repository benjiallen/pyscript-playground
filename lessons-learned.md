# Lessons learned

## First steps

### Use a basic server

Using the `file:///` protocol seems problematic when trying to load an external python file. It causes a [CORS request not HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSRequestNotHttp) error.

The solution to this problem seems to be using a basic server to serve the files. Open the terminal and `cd` to the project root. Run `python -m http.server`.

### Documentation for PyScript

[PyScript Docs](https://docs.pyscript.net/latest/index.html) are not very useful right now.

There doesn't seem to be a well defined API where I can look up the features of pyscript. For example, I know the `Element` class has a `write` method but what else does it have?

GitHub offers some clues. See [pyscript.py](https://github.com/pyscript/pyscript/blob/main/pyscriptjs/src/python/pyscript.py). Would be good if they used type hints!

Other useful references:

- [pyodide: Importing JavaScript objects into Python](https://pyodide.org/en/stable/usage/type-conversions.html#importing-javascript-objects-into-python)
- [JavaScript Document API](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [JavaScript Element API](https://developer.mozilla.org/en-US/docs/Web/API/Element)

## File system access

You can't just read a file from the file system like you would with regular python. The following example will lead to an error.

```python
import json

with open('file.json') as read_file:
    json.load(read_file)
```

Good articles on the topic:

- [Pyscript: Files and File Systems – Part 1](https://www.jhanley.com/blog/pyscript-files-and-file-systems-part-1/)
- [Pyscript: Files and File Systems – Part 2](https://www.jhanley.com/blog/pyscript-files-and-file-systems-part-2/)

In my case, I was trying to load a `JSON` file. I loaded the JSON by making it a JavaScript variable and loading the JavaScript with a `<script>` tag.

```html
<script src="./python-org-data.js"></script>
```

This technique also taught me how to pass JavaScript objects into my python code. See [PyScript: JavaScript and Python Interoperability](https://www.jhanley.com/blog/pyscript-javascript-and-python-interoperability/).

## Assigning event handlers

[Pyscript: JavaScript Event Callbacks](https://www.jhanley.com/blog/pyscript-javascript-callbacks/).

Updte: things are changing all the time, now there is a new method. [Whats New in Pyscript 2022.09.1](https://jeff.glass/post/whats-new-pyscript-2022-09-1/). Uses `add_event_listener`.

## Loading 3rd party packages

You get the python standard library for free. You can easily access other 3rd party libraries if they [shipped with pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html). If you need something outside of those libraries then you can install pure python libraries if those libraries have a wheel file `.whl`. If you can get hold of a wheel then you can reference the wheel from `<pyconfig>`.

Useful articles:

- [Packages built in Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)
- [pyconfig tag](https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag)

## Using print()

Writes to console.log()
