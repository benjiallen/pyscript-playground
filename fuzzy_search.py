"""
Example of using a module from pypi.

I want to use https://pypi.org/project/fuzzywuzzy/ to do fuzzy matching.

Useful article on using events in pyscript:
https://www.jhanley.com/blog/pyscript-javascript-callbacks/

Articles on loading 3rd party packages:
* https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages
* https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag

TODO:
* Improve the case where there are no results found.
* Figure out the different views
  - exact match then show more details
  - non-exact match then show the possible matches "did you mean?"

"""
import json
from js import document
from pyodide.ffi import create_proxy
from thefuzz import process

people_json: str = """
[
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Peter", "age": 27},
    {"name": "Susan", "age": 25},
    {"name": "Ben", "age": 27},
    {"name": "benji", "age": 27},
    {"name": "benjamin", "age": 27},
    {"name": "benjiallen", "age": 27},
    {"name": "allen ben", "age": 27}
]
"""

data = json.loads(people_json)
data_t = None
tbody = document.querySelector("#employees tbody")
template = document.querySelector('#employee')

def tranform_data(data):
    """Transform the data such that each employee is a dict entry.
    The key is the name and the value is the age."""
    return {person['name']: person['age'] for person in data}

def add_rows_to_table(rows, clear_table=False):
    """Add the rows to the table."""
    if clear_table:
        tbody.innerHTML = ''
        # TODO: add a row that says no results found
    for row in rows:
        # Clone the new row and insert it into the table
        clone = template.content.cloneNode(True)
        td = clone.querySelectorAll('td')
        td[0].textContent = row['name']
        td[1].textContent = row['age']
        tbody.appendChild(clone)

def search_handler(event):
    """Does something when the search button is activated.
    proccess module within thefuzz package seems like a great fit!
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175
    """
    # Get the value from the search field and to table
    search_value: str = document.getElementById("search").value
    # returns a list of tuples
    extracted = process.extractBests(search_value, data_t.keys(),
                                     score_cutoff=50, limit=5)
    results = []
    for name, score in extracted:
        result = {}
        result['name'] = f'{name}, {score}'
        result['age'] = data_t[name]
        results.append(result)
    add_rows_to_table(results, clear_table=True)

def setup():
    """Setup the page."""
    global data_t
    data_t = tranform_data(data)
    add_rows_to_table(data)

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(search_handler)

    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click", click_proxy)

setup()
