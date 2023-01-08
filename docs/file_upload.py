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
from js import document
from pyodide.ffi.wrappers import add_event_listener


async def upload_handler(event) -> None:
    """Event handler that runs when the upload button is activated."""
    # don't send the form over the network!
    event.preventDefault()

    file_uploader = document.getElementById("file")

    files = file_uploader.files.to_py()

    for f in files:
        data = await f.text()
        document.getElementById("results").innerHTML = data

    # TODO:
    # 1. Write the contents of the file to a global variable
    # 2. Write the next view to the DOM and make sure event listeners are setup
    #    - Not sure how program flow works when i get to the end of an async function
    # 3. Use the code already have to handle search interaction from there 

def setup() -> None:
    """Setup the page."""
    add_event_listener(document.getElementById("upload-action"),
                       "click",
                       upload_handler)

setup()
