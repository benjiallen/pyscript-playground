"""
Example of using a module from pypi.

I want to use https://pypi.org/project/fuzzywuzzy/ to do fuzzy matching.

Useful article on using events in pyscript:
https://www.jhanley.com/blog/pyscript-javascript-callbacks/

Articles on loading 3rd party packages:
* https://pyodide.org/en/stable/usage/loading-packages.html#loading-packages
* https://docs.pyscript.net/latest/tutorials/getting-started.html#the-py-config-tag

TODO:
* Deploy to GitHub pages
* Get feedback on what i've built so far!
* Search by name and handle
* Work out how to add searches to browser history
* Add python typing information
* Add an "upload file" mode where you can upload a YAML file with the org chart
* Write some playwright tests

handle:
    - name: full name
    - title: job title
    - email: email address
    - manager: handle
    - employment_type: employee
    - cost_center: cost center
    - country: country
"""
from js import document
from js import org_chart_data
from pyodide.ffi import create_proxy
from thefuzz import process

data = org_chart_data[0].to_py()
results = document.getElementById('results')
no_result = document.getElementById('no-results')
exact_match = document.getElementById('exact-match')
close_match = document.getElementById('close-match')
close_match_item = document.getElementById('close-match-item')

def search_handler(event, search_term:str='', focus_target_id:str=''):
    """Does something when the search button is activated.
    proccess module within thefuzz package seems like a great fit!
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175
    """
    # don't send the form over the network!
    event.preventDefault()
    if not search_term:
        search_term:str = document.getElementById("search").value
    else:
        document.getElementById("search").value = search_term
    # returns a list of tuples
    extracted:list[tuple[str,int]] = process.extractBests(search_term, data.keys(),
                                     score_cutoff=60, limit=5)
    results.innerHTML = ''
    """
    Different cases to think of:
    1. No results
    2. Exact match only
    3. Exact match and close matches
    4. Close matches only
    """
    if extracted:
        best_name, best_score = extracted[0]
        if best_score == 100:
            extracted.pop(0)
            exact_match_clone = exact_match.content.cloneNode(True)
            exact_match_clone.querySelectorAll('p')[0].textContent = best_name
            # populate the rest of the data
            exact_match_clone.getElementById('name').textContent = data[best_name]['name'] if data[best_name]['name'] else 'No name available'
            exact_match_clone.getElementById('title').textContent = data[best_name]['title'] if data[best_name]['title'] else 'No title available'
            exact_match_clone.getElementById('email').textContent = data[best_name]['email'] if data[best_name]['email'] else 'No email available'
            if 'manager' in data[best_name]:
                button = exact_match_clone.querySelectorAll('#manager button')[0]
                button.textContent = data[best_name]['manager']
                click_proxy = create_proxy(search_from_button)
                button.addEventListener("click", click_proxy)
            else:
                exact_match_clone.getElementById('manager').textContent = 'No manager'
            # TODO: move the find_directs call to setup()
            reports = find_directs(best_name)
            reports_out = exact_match_clone.getElementById('reports')
            if reports:
                list_of_reports = document.createElement('ol')
                for report in reports:
                    report_item = close_match_item.content.cloneNode(True)
                    report_button = report_item.querySelectorAll('button')[0]
                    report_button.textContent = report
                    click_proxy = create_proxy(search_from_button)
                    report_button.addEventListener("click", click_proxy)
                    list_of_reports.appendChild(report_item)
                reports_out.appendChild(list_of_reports)
            else:
                message = document.createElement('p')
                message.textContent = 'No reports'
                reports_out.appendChild(message)
            exact_match_clone.getElementById('cost-center').textContent = data[best_name]['cost_center'] if data[best_name]['cost_center'] else 'No cost center available'
            exact_match_clone.getElementById('country').textContent = data[best_name]['country'] if data[best_name]['country'] else 'No country available'
            exact_match_clone.getElementById('employment-type').textContent = data[best_name]['employment_type'] if data[best_name]['employment_type'] else 'No employment type available'
            results.appendChild(exact_match_clone)
            results.appendChild(exact_match_clone)
        # TODO: need to refactor if possible, prefer to not have 2 checks for extracted
        if extracted:
            close_match_clone = close_match.content.cloneNode(True)
            list_parent = close_match_clone.querySelectorAll('ul')[0]
            for name, score in extracted:
                close_match_item_clone = close_match_item.content.cloneNode(True)
                button = close_match_item_clone.querySelectorAll('button')[0]
                # button.textContent = f'{name}, {score}'
                button.textContent = name
                click_proxy = create_proxy(search_from_button)
                button.addEventListener("click", click_proxy)
                list_parent.appendChild(close_match_item_clone)
            results.appendChild(close_match_clone)
    else:
        results.appendChild(no_result.content.cloneNode(True))
    if focus_target_id:
        document.getElementById(focus_target_id).focus()

def search_from_button(event):
    """Search from the button."""
    search_term:str = event.target.textContent
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='exact-match-heading')

def find_directs(handle:str) -> list[str]:
    """Find the direct reports for a given handle."""
    return [k for k, v in data.items() if v.get('manager', '') == handle]

def setup():
    """Setup the page."""
    # TODO: find all the directs for each handle and store in a dict
    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click",
                                                              create_proxy(search_handler))

setup()
