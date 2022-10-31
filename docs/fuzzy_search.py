"""
Creates an interactive and accessible org chart based on data in python-org-data.js

Uses thefuzz package to search the org chart data.
https://github.com/seatgeek/thefuzz
https://pypi.org/project/thefuzz/

TODO:
* Get feedback on what i've built so far!
* Work out how to add searches to browser history
* Add python typing information
* Add an "upload file" mode where you can upload a YAML file with the org chart
* Experiment with the idea of a "layered" application where all data structure work
  is one part of the application and can be run independently of the browser. This has
  the benefit of letting me use testing and debugging tools within VS Code.
  It does mean that I will have to setup an environment with the right packages installed!

handle:
    - name: full name
    - title: job title
    - email: email address
    - manager: handle
    - employment_type: employee
    - cost_center: cost center
    - country: country
"""
import itertools
from collections import defaultdict
from typing import DefaultDict, Iterable, Optional, OrderedDict
import bleach
from js import document
from js import org_chart_data
from pyodide.ffi.wrappers import add_event_listener, set_timeout
from thefuzz import process

data:dict[str, dict[str, str]] = org_chart_data[0].to_py()
names:DefaultDict[str, list[str]] = defaultdict(list)
for k, v in data.items():
    names[v['name']].append(k)
names_and_handles:list[str] = list(names.keys()) + list(data.keys())

results = document.getElementById('results')
no_result = document.getElementById('no-results')
exact_match = document.getElementById('exact-match')
close_match = document.getElementById('close-match')
close_match_item = document.getElementById('close-match-item')
duplicate_name = document.getElementById('duplicate-name')
notify = document.getElementById('notify')

def search_handler(event, search_term:str='', focus_target_id:str='') -> None:
    """Does something when the search button is activated.
    Uses the proccess module within thefuzz package to find good search results.
    https://github.com/seatgeek/thefuzz/blob/master/thefuzz/process.py#L175

    General idea here:

    1. Work on getting data structures right
    2. Pass the data structures to functions that can write to the DOM
    """
    # don't send the form over the network!
    event.preventDefault()

    if not search_term:
        search_term = bleach.clean(document.getElementById("search").value)
    else:
        document.getElementById("search").value = search_term
    
    # perform the search
    extracted:list[tuple[str,int]] = process.extractBests(search_term,
                                                          names_and_handles,
                                                          score_cutoff=61,
                                                          limit=5)
    results.innerHTML = ''
    """
    Different cases to think of:
    1. No results
    2. Exact match only
    3. Exact match and close matches
    4. Close matches only
    5. One name with multiple handles
    """
    if extracted:
        best_name, best_score = extracted[0]
        duplicate = False
        # is the best match a name or a handle?
        if best_name not in data:
            # deal with the case where the name is a duplicate
            if len(names[best_name]) > 1 and best_score == 100:
                duplicate = True
                duplicate_name_clone = duplicate_name.content.cloneNode(True)
                write_list(duplicate_name_clone,
                           'ul',
                           close_match_item,
                           zip(itertools.repeat(best_name,
                                                len(names[best_name])),
                               names[best_name]))
                results.appendChild(duplicate_name_clone)
            else:
                # name is not a duplicate, so get the handle
                best_name = names[best_name][0]
        # exact match
        if best_score == 100 and not duplicate:
            extracted.pop(0)
            exact_match_clone = exact_match.content.cloneNode(True)
            exact_match_clone.querySelectorAll('p')[0].textContent = best_name
            # populate the rest of the data
            write_details(exact_match_clone, data[best_name])
            if 'manager' in data[best_name]:
                button = exact_match_clone.querySelectorAll('#manager button')[0]
                button.textContent = (f"{data[best_name]['manager']}, "
                                      f"{data[data[best_name]['manager']]['name']}")
                button.value = data[best_name]['manager']
                add_event_listener(button, "click", search_from_button)
            else:
                exact_match_clone.getElementById('manager').textContent = 'No manager'
            # TODO: move the find_directs call to setup()
            reports = find_directs(best_name)
            reports_out = exact_match_clone.getElementById('reports')
            if reports:
                write_list(reports_out, 'ol', close_match_item, reports)
            else:
                message = document.createElement('p')
                message.textContent = 'No reports'
                reports_out.appendChild(message)
            results.appendChild(exact_match_clone)
        # TODO: need to refactor if possible, prefer to not have 2 checks for extracted
        # close matches, we use an OrderedDict to preserve the order of the results
        combined:Optional[OrderedDict[str, str]] = None
        if extracted:
            # handles map to names
            combined = OrderedDict()
            for result, _ in extracted:
                if result in data:
                    # it's a handle, handles are unique
                    combined[result] = data[result]["name"]
                else:
                    # it's a name, names are not unique so we need
                    # to add all the handles that share the name
                    for handle in names[result]:
                        combined[handle] = data[handle]["name"]
            # need to remove the best match from the dict
            if best_score == 100:
                # when the handles are similar to the name then the name
                # can end up in the combined dict
                # when the handles are not similar to the name then a key error
                # is likely and that's fine
                try:
                    if duplicate:
                        for handle in names[best_name]:
                            del combined[handle]
                    else:
                        del combined[best_name]
                except KeyError:
                    pass
        # write the close matches
        if combined:
            close_match_clone = close_match.content.cloneNode(True)
            write_list(close_match_clone, 'ul', close_match_item, combined.items())
            results.appendChild(close_match_clone)
    # no results
    else:
        results.appendChild(no_result.content.cloneNode(True))
    if focus_target_id:
        document.getElementById(focus_target_id).focus()
    else:
        # have to empty the text, wait, then populate the text
        # so that the screen reader will read the text
        sr_notification('')
        set_timeout(sr_notification, 300)

def sr_notification(note:str='Search complete') -> None:
    """Notify the user that the search is complete."""
    notify.textContent = note

def search_from_button(event) -> None:
    """Event handler that runs when a button with a handle is activated."""
    search_term:str = event.target.value
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='exact-match-heading')

def find_directs(handle:str) -> list[tuple[str, str]]:
    """Find the direct reports for a given handle and return the sorted list."""
    reports = [(k, data[k]['name']) for k, v in data.items() if v.get('manager', '') == handle]
    return sorted(reports, key=lambda x: x[1].lower())

def write_details(parent_node, employee:dict[str, str | None]) -> None:
    ids_keys_labels = (('name', 'name', 'No name available'),
                       ('title', 'title', 'No title available'),
                       ('email', 'email', 'No email available'),
                       ('cost-center', 'cost_center', 'No cost center available'),
                       ('country', 'country', 'No country available'),
                       ('employment-type', 'employment_type', 'No employment type available'),
                      )
    for id, key, label in ids_keys_labels:
        node = parent_node.getElementById(id)
        if employee[key]:
            node.textContent = employee[key]
        else:
            node.textContent = label

def write_list(parent_node,
               html_list_type:str,
               list_item_template,
               data:Iterable[tuple[str, str]]) -> None:
    if match := parent_node.querySelectorAll(html_list_type):
        list_parent = match[0]
    else:
        list_parent = document.createElement(html_list_type)
        parent_node.appendChild(list_parent)
    for handle, name in data:
        item_clone = list_item_template.content.cloneNode(True)
        button = item_clone.querySelectorAll('button')[0]
        button.textContent = f'{handle}, {name}'
        button.value = handle
        add_event_listener(button, "click", search_from_button)
        list_parent.appendChild(item_clone)

def setup() -> None:
    """Setup the page."""
    # TODO: find all the directs for each handle and store in a dict
    add_event_listener(document.getElementById("search-action"),
                       "click",
                       search_handler)

setup()
