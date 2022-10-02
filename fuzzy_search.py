"""
Example of using a module from pypi.

I want to use https://pypi.org/project/fuzzywuzzy/ to do fuzzy matching.

Useful article on using events in pyscript:
https://www.jhanley.com/blog/pyscript-javascript-callbacks/

TODO:
* work out how to find the wheel file for the thefuzz package.
https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages
* then add the wheel using the <py-config> tag
https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag
* then work out how to use fuzzywuzzy to find search results    
"""
import json
from js import document
from pyodide.ffi import create_proxy
from thefuzz import fuzz

people_json: str = """
[
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Peter", "age": 27},
    {"name": "Susan", "age": 25},
    {"name": "Ben", "age": 27}
]
"""

data = json.loads(people_json)
tbody = document.querySelector("#employees tbody")
template = document.querySelector('#employee')

def add_rows_to_table(rows):
    """Add the rows to the table."""
    for row in rows:
        # Clone the new row and insert it into the table
        clone = template.content.cloneNode(True)
        td = clone.querySelectorAll('td')
        td[0].textContent = row['name']
        td[1].textContent = row['age']
        tbody.appendChild(clone)

def search_handler(event):
    """Does something when the search button is activated."""
    # TODO: replace this test with the search algorithm
    tester = {
                "name": "Test",
                "age": 100,
             }
    # Get the value from the search field and to table
    search_value: str = document.getElementById("search").value
    if search_value:
        tester['name'] = search_value
        tester['age'] = fuzz.ratio(search_value, f'{search_value}!!!')
    add_rows_to_table([tester])

def setup():
    """Setup the page."""
    add_rows_to_table(data)

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(search_handler)

    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click", click_proxy)

setup()
