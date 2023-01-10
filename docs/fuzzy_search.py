"""
Creates an interactive and accessible org chart based on data in python-org-data.js

Uses thefuzz package to search the org chart data.
https://github.com/seatgeek/thefuzz
https://pypi.org/project/thefuzz/

TODO:
* Get feedback on what i've built so far!
* Work out how to add searches to browser history
* Add python typing information
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
import json
from collections import defaultdict, deque
from typing import DefaultDict, Optional, OrderedDict
import bleach
from jinja2 import Environment, FileSystemLoader, select_autoescape
from js import document
from js import org_chart_data
from js import localStorage
from pyodide.ffi.wrappers import add_event_listener, set_timeout
from thefuzz import process

data:dict[str, dict[str, str]]
if localStorage.getItem("data"):
    data = json.loads(localStorage.getItem("data"))[0]
else:
    data = org_chart_data[0].to_py()
names:DefaultDict[str, list[str]] = defaultdict(list)
for k, v in data.items():
    names[v['name']].append(k)
names_and_handles:list[str] = list(names.keys()) + list(data.keys())

env = Environment(
    loader = FileSystemLoader("./"),
    autoescape=select_autoescape()
)

results = document.getElementById('results')
notify = document.getElementById('notify')
previous_searches = document.getElementById('previous-searches')

history:deque[str] = deque(maxlen=5)

def search_handler(event, search_term:str='', focus_target_id:str='') -> None:
    # don't send the form over the network!
    event.preventDefault()

    if not search_term:
        search_term = bleach.clean(document.getElementById("search").value)
    else:
        document.getElementById("search").value = search_term
    add_previous_search(search_term)

    # perform the search
    extracted:list[tuple[str,int]] = process.extractBests(search_term,
                                                          names_and_handles,
                                                          score_cutoff=61,
                                                          limit=5)
    results.innerHTML = ''
    results_for_templates:list[str] = []
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
                dn_template = env.get_template("duplicate_name.j2")
                duplicate_names = zip(itertools.repeat(best_name,len(names[best_name])),
                                                       names[best_name])
                results_for_templates.append(dn_template.render(data=duplicate_names))
            else:
                # name is not a duplicate, so get the handle
                best_name = names[best_name][0]
        # exact match
        if best_score == 100 and not duplicate:
            extracted.pop(0)
            em_template = env.get_template("exact_match.j2")
            manager = {}
            if 'manager' in data[best_name]:
                manager['handle'] = data[best_name]['manager']
                manager['name'] = data[data[best_name]['manager']]['name']
            # TODO: move the find_directs call to setup()
            results_for_templates.append(em_template.render(best_name=best_name,
                                                            employee=data[best_name],
                                                            manager=manager,
                                                            reports=find_directs(best_name)))
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
            cm_template = env.get_template("close_match.j2")
            results_for_templates.append(cm_template.render(data=combined.items()))
    # no results
    else:
        nr_template = env.get_template("no_result.j2")
        results_for_templates.append(nr_template.render())
    # write the results
    results.innerHTML = '\n'.join(results_for_templates)
    # add event listeners (setting the HTML with innerHTML removes them)
    add_event_listeners_to_buttons('#results button', search_from_button)
    if focus_target_id:
        document.getElementById(focus_target_id).focus()
    else:
        # have to empty the text, wait, then populate the text
        # so that the screen reader will read the text
        sr_notification('')
        set_timeout(sr_notification, 300)

def add_previous_search(search_term:str) -> None:
    if history:
        ps_template = env.get_template("previous_search.j2")
        previous_searches.innerHTML = ps_template.render(history=reversed(history))
        add_event_listeners_to_buttons('#previous-searches button', search_from_history)
    if search_term:
        history.append(search_term)

def add_event_listeners_to_buttons(selector:str, handler) -> None:
    """Adds event listeners to all the buttons in the DOM."""
    buttons = document.querySelectorAll(selector)
    for button in buttons:
        add_event_listener(button, 'click', handler)

def sr_notification(note:str='Search complete') -> None:
    """Notify the user that the search is complete."""
    notify.textContent = note

def search_from_button(event) -> None:
    """Event handler that runs when a button with a handle is activated."""
    search_term:str = event.target.value
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='exact-match-heading')

def search_from_history(event) -> None:
    """Event handler that runs when a button with a previous search is activated."""
    search_term:str = event.target.value
    search_handler(event,
                   search_term=search_term,
                   focus_target_id='search')

def find_directs(handle:str) -> list[tuple[str, str]]:
    """Find the direct reports for a given handle and return the sorted list."""
    reports = [(k, data[k]['name']) for k, v in data.items() if v.get('manager', '') == handle]
    return sorted(reports, key=lambda x: x[1].lower())

def setup() -> None:
    """Setup the page."""
    # TODO: find all the directs for each handle and store in a dict
    add_event_listener(document.getElementById("search-action"),
                       "click",
                       search_handler)

setup()
