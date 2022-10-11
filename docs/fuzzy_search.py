"""
Creates an interactive and accessible org chart based on data in python-org-data.js

Uses thefuzz package to search the org chart data.
https://github.com/seatgeek/thefuzz
https://pypi.org/project/thefuzz/

TODO:
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

data:dict[str, dict[str, str]] = org_chart_data[0].to_py()
results = document.getElementById('results')
no_result = document.getElementById('no-results')
exact_match = document.getElementById('exact-match')
close_match = document.getElementById('close-match')
close_match_item = document.getElementById('close-match-item')

def search_handler(event, search_term:str='', focus_target_id:str=''):
    """Does something when the search button is activated.
    Uses the proccess module within thefuzz package to find good search results.
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175
    """
    # don't send the form over the network!
    event.preventDefault()
    if not search_term:
        search_term = document.getElementById("search").value
    else:
        document.getElementById("search").value = search_term
    # perfrom the search
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
            write(exact_match_clone,
                  'name',
                  data[best_name]['name'],
                  'No name available')
            write(exact_match_clone,
                  'title',
                  data[best_name]['title'],
                  'No title available')
            write(exact_match_clone,
                  'email',
                  data[best_name]['email'],
                  'No email available')
            if 'manager' in data[best_name]:
                button = exact_match_clone.querySelectorAll('#manager button')[0]
                button.textContent = data[best_name]['manager']
                button.addEventListener("click",
                                        create_proxy(search_from_button))
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
                    report_button.addEventListener("click",
                                                   create_proxy(search_from_button))
                    list_of_reports.appendChild(report_item)
                reports_out.appendChild(list_of_reports)
            else:
                message = document.createElement('p')
                message.textContent = 'No reports'
                reports_out.appendChild(message)
            write(exact_match_clone,
                  'cost-center',
                  data[best_name]['cost_center'],
                  'No cost center available')
            write(exact_match_clone,
                  'country',
                  data[best_name]['country'],
                  'No country available')
            write(exact_match_clone,
                  'employment-type',
                  data[best_name]['employment_type'],
                  'No employment type available')
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
                button.addEventListener("click",
                                        create_proxy(search_from_button))
                list_parent.appendChild(close_match_item_clone)
            results.appendChild(close_match_clone)
    else:
        results.appendChild(no_result.content.cloneNode(True))
    if focus_target_id:
        document.getElementById(focus_target_id).focus()

def search_from_button(event):
    """Event handler that runs when a button with a handle is activated."""
    search_term:str = event.target.textContent
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='exact-match-heading')

def find_directs(handle:str) -> list[str]:
    """Find the direct reports for a given handle."""
    return [k for k, v in data.items() if v.get('manager', '') == handle]

def write(parent_node, id:str, text:str, default_text:str):
    """Write to the DOM."""
    if text:
        parent_node.getElementById(id).textContent = text
    else:
        parent_node.getElementById(id).textContent = default_text

def setup():
    """Setup the page."""
    # TODO: find all the directs for each handle and store in a dict
    # Set the listener to the callback
    document.getElementById("search-action").addEventListener("click",
                                                              create_proxy(search_handler))

setup()
