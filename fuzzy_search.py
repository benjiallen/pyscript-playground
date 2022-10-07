"""
Example of using a module from pypi.

I want to use https://pypi.org/project/fuzzywuzzy/ to do fuzzy matching.

Useful article on using events in pyscript:
https://www.jhanley.com/blog/pyscript-javascript-callbacks/

Articles on loading 3rd party packages:
* https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages
* https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag

TODO:
* Figure out the proper shape of the data
* Work out how you can traverse the org chart - viewing directs, viewing managers
* Think about where focus should go.
"""
import json
from js import document
from pyodide.ffi import create_proxy
from thefuzz import process

people_json: str = """
[
    {"name": "gvanrossum", "age": 1},
    {"name": "freddrake", "age": 1},
    {"name": "birkenfeld", "age": 1},
    {"name": "vstinner", "age": 1},
    {"name": "benjaminp", "age": 1},
    {"name": "rhettinger", "age": 1},
    {"name": "pitrou", "age": 1},
    {"name": "jackjansen", "age": 1},
    {"name": "serhiy-storchaka", "age": 1},
    {"name": "loewis", "age": 1},
    {"name": "tim-one", "age": 1},
    {"name": "akuchling", "age": 1},
    {"name": "warsaw", "age": 1},
    {"name": "brettcannon", "age": 1},
    {"name": "nnorwitz", "age": 1},
    {"name": "mdickinson", "age": 1},
    {"name": "tiran", "age": 1},
    {"name": "bitdancer", "age": 1},
    {"name": "ezio-melotti", "age": 1},
    {"name": "gpshead", "age": 1},
    {"name": "jeremyhylton", "age": 1},
    {"name": "vsajip", "age": 1},
    {"name": "orsenthil", "age": 1},
    {"name": "terryjreedy", "age": 1},
    {"name": "gward", "age": 1},
    {"name": "merwok", "age": 1},
    {"name": "zooba", "age": 1},
    {"name": "ned-deily", "age": 1},
    {"name": "ncoghlan", "age": 1},
    {"name": "pablogsal", "age": 1},
    {"name": "1st1", "age": 1},
    {"name": "ronaldoussoren", "age": 1},
    {"name": "berkerpeksag", "age": 1},
    {"name": "doerwalter", "age": 1},
    {"name": "kbkaiser", "age": 1},
    {"name": "amauryfa", "age": 1},
    {"name": "zware", "age": 1},
    {"name": "ericvsmith", "age": 1},
    {"name": "asvetlov", "age": 1},
    {"name": "vadmium", "age": 1},
    {"name": "erlend-aasland", "age": 1},
    {"name": "briancurtin", "age": 1},
    {"name": "skrah", "age": 1},
    {"name": "florentx", "age": 1},
    {"name": "abalkin", "age": 1},
    {"name": "Yhg1s", "age": 1},
    {"name": "larryhastings", "age": 1},
    {"name": "malemburg", "age": 1},
    {"name": "nascheme", "age": 1},
    {"name": "methane", "age": 1},
    {"name": "doko42", "age": 1},
    {"name": "avassalotti", "age": 1},
    {"name": "eliben", "age": 1},
    {"name": "ZackerySpytz", "age": 1},
    {"name": "markshannon", "age": 1},
    {"name": "ericsnowcurrently", "age": 1},
    {"name": "corona10", "age": 1},
    {"name": "voidspace", "age": 1},
    {"name": "giampaolo", "age": 1},
    {"name": "jcea", "age": 1},
    {"name": "iritkatriel", "age": 1},
    {"name": "ethanfurman", "age": 1},
    {"name": "sandrotosi", "age": 1},
    {"name": "jaraco", "age": 1},
    {"name": "anthonybaxter", "age": 1},
    {"name": "collinw", "age": 1},
    {"name": "ambv", "age": 1},
    {"name": "nvawda", "age": 1},
    {"name": "andresdelfino", "age": 1},
    {"name": "facundobatista", "age": 1},
    {"name": "shibturn", "age": 1},
    {"name": "mhammond", "age": 1},
    {"name": "sjoerdmullender", "age": 1},
    {"name": "gustaebel", "age": 1},
    {"name": "hyeshik", "age": 1},
    {"name": "csabella", "age": 1},
    {"name": "isidentical", "age": 1},
    {"name": "brandtbucher", "age": 1},
    {"name": "sobolevn", "age": 1},
    {"name": "JulienPalard", "age": 1},
    {"name": "shihai1991", "age": 1},
    {"name": "akheron", "age": 1},
    {"name": "Fidget-Spinner", "age": 1},
    {"name": "kumaraditya303", "age": 1},
    {"name": "zestyping", "age": 1},
    {"name": "jnoller", "age": 1},
    {"name": "cjerdonek", "age": 1},
    {"name": "encukou", "age": 1},
    {"name": "eric-s-raymond", "age": 1},
    {"name": "cloud-tester", "age": 1},
    {"name": "sweeneyde", "age": 1},
    {"name": "jyasskin", "age": 1},
    {"name": "cf-natali", "age": 1},
    {"name": "tirkarthi", "age": 1},
    {"name": "gpolo", "age": 1},
    {"name": "zhangyangyu", "age": 1},
    {"name": "lysnikolaou", "age": 1},
    {"name": "tpn", "age": 1},
    {"name": "Mariatta", "age": 1},
    {"name": "taleinat", "age": 1}
]
"""

data = json.loads(people_json)
data_t = None
results = document.getElementById('results')
no_result = document.getElementById('no-results')
exact_match = document.getElementById('exact-match')
close_match = document.getElementById('close-match')
close_match_item = document.getElementById('close-match-item')

def tranform_data(data):
    """Transform the data such that each employee is a dict entry.
    The key is the name and the value is the age."""
    return {person['name']: person['age'] for person in data}

def search_handler(event, search_term:str=''):
    """Does something when the search button is activated.
    proccess module within thefuzz package seems like a great fit!
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175
    """
    # don't send the form over the network!
    event.preventDefault();
    if not search_term:
        search_term = document.getElementById("search").value
    else:
        document.getElementById("search").value = search_term
    # returns a list of tuples
    extracted = process.extractBests(search_term, data_t.keys(),
                                     score_cutoff=50, limit=5)
    results.innerHTML = ''
    if extracted:
        best_name, best_score = extracted[0]
        if best_score == 100:
            extracted.pop(0)
            exact_match_clone = exact_match.content.cloneNode(True)
            exact_match_clone.querySelectorAll('p')[0].textContent = best_name
            results.appendChild(exact_match_clone)
        close_match_clone = close_match.content.cloneNode(True)
        list_parent = close_match_clone.querySelectorAll('ul')[0]
        for name, score in extracted:
            # add list items to the list
            close_match_item_clone = close_match_item.content.cloneNode(True)
            button = close_match_item_clone.querySelectorAll('button')[0]
            button.textContent = f'{name}, {score}'
            click_proxy = create_proxy(search_from_button)
            button.addEventListener("click", click_proxy)
            list_parent.appendChild(close_match_item_clone)
        results.appendChild(close_match_clone)
    else:
        results.appendChild(no_result.content.cloneNode(True))

def search_from_button(event):
    """Search from the button."""
    search_term = event.target.textContent.split(',')[0]
    search_handler(event, search_term=search_term)

def setup():
    """Setup the page."""
    global data_t
    data_t = tranform_data(data)

    # Create a JsProxy for the callback function
    click_proxy = create_proxy(search_handler)

    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click", click_proxy)

setup()
