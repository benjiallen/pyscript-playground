"""
Example of using a module from the python standard library.
"""
import json
from js import document

people_json: str = """
[
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Peter", "age": 27},
    {"name": "Susan", "age": 25},
    {"name": "Ben", "age": 27}
]
"""

# https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
# Instantiate the table with the existing HTML tbody and the row with the template
tbody = document.querySelector("#employees tbody")
template = document.querySelector('#employee')

for person in json.loads(people_json):
    # Clone the new row and insert it into the table
    clone = template.content.cloneNode(True)
    td = clone.querySelectorAll('td')
    td[0].textContent = person['name']
    td[1].textContent = person['age']
    tbody.appendChild(clone)

# can't do this because of browser sandboxing
# with open('people.json') as json_file:
#     data = json.load(json_file)
#     output.write(data)
# example of loading data over the network
# will definitely require some research!
# https://pyodide.org/en/stable/usage/api/python-api/http.html#pyodide.http.pyfetch
# https://www.jhanley.com/blog/pyscript-getting-application-data/
# https://docs.pyscript.net/latest/howtos/http-requests.html

# another idea for trying to do it in HTML
# add the data as a JS file and then refer to that variable
# https://stackoverflow.com/questions/18637418/trying-to-load-local-json-file-to-show-data-in-a-html-page-using-jquery
