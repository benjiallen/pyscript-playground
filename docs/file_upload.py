"""
Challenges:

1. Working with asyncio
2. Can you write files to the virtual file system?
3. How do you share state between pages? Can I write in 1 page and read from another?

Alternatives to persisting state:

1. Just keep the data within the file within memory
   - The file upload code would have to live in the same place as the code that uses the file data
   - I'd have to write code that handles more page states
     i.e., the page that uploads the file and the page that uses the file
"""

import asyncio
import json
from js import document
from js import localStorage
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pyodide.ffi.wrappers import add_event_listener

json_data = None

env = Environment(
    loader = FileSystemLoader("./"),
    autoescape=select_autoescape()
)

async def upload_handler(event) -> None:
    """Event handler that runs when the upload button is activated."""
    # don't send the form over the network!
    event.preventDefault()
    file_uploader = document.getElementById("file")
    files = file_uploader.files.to_py()
    for f in files:
        data = await f.text()
        global json_data
        json_data = data
    localStorage.setItem("data", json_data)
    write_page()

def write_page() -> None:
    """Write the page to the DOM."""
    template = env.get_template("upload_success.j2")
    rendered = template.render()
    document.getElementById("results").innerHTML = rendered

def setup() -> None:
    """Setup the page."""
    add_event_listener(document.getElementById("upload-action"),
                       "click",
                       upload_handler)

setup()
