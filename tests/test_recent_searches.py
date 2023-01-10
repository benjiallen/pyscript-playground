from playwright.sync_api import Page, expect

def test_no_recents_on_first_load(page: Page) -> None:
    """
    When the page has loaded for the first time
    Then there is no previous search history
    """
    page.goto("http://0.0.0.0:8000/docs/search.html")
    expect(page.get_by_role("heading", name="Recent searches")).not_to_be_visible()

def test_no_recents_on_first_search(page: Page) -> None:
    """
    Given I am navigating the org chart
    When I search for the first time
    And receive results
    Then there is no previous search history
    """
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("first")
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("heading", name="Recent searches")).not_to_be_visible()

def test_recents_on_second_search(page: Page) -> None:
    """
    Given I am navigating the org chart
    And I have completed a search
    When I search for the second time
    And receive results
    Then there is one previous search
    And the previous search is the first search term
    """
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("first")
    page.get_by_role("button", name="Search").click()
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("second")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("#previous-searches-list > li > button")).to_have_text("first")

def test_recents_on_sixth_search(page: Page) -> None:
    """
    Given I am navigating the org chart
    And I have completed five searches
    When I search for the sixth time
    And receive results
    Then there are five previous searches
    And the previous searches are the first five search terms
    """
    searches = ("first", "second", "third", "fourth", "fifth", "sixth")
    page.goto("http://0.0.0.0:8000/docs/search.html")
    for search in searches:
        page.get_by_label("Search by name").click()
        page.get_by_label("Search by name").fill(search)
        page.get_by_role("button", name="Search").click()
    buttons = page.locator("#previous-searches-list > li > button").all_inner_texts()
    # reverse the searches list because the recent search history is a stack
    # the most recent search is at the top of the list
    for button_text, search in zip(buttons, reversed(searches[:-1])):
        assert button_text == search

def test_recents_on_seventh_search(page: Page) -> None:
    """
    Given I am navigating the org chart
    And I have completed six searches
    When I search for the seventh time
    And receive results
    Then there are five previous searches
    And the previous searches are the second to sixth search terms
    """
    searches = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh")
    page.goto("http://0.0.0.0:8000/docs/search.html")
    for search in searches:
        page.get_by_label("Search by name").click()
        page.get_by_label("Search by name").fill(search)
        page.get_by_role("button", name="Search").click()
    buttons = page.locator("#previous-searches-list > li > button").all_inner_texts()
    # reverse the searches list because the recent search history is a stack
    # the most recent search is at the top of the list
    for button_text, search in zip(buttons, reversed(searches[1:-1])):
        assert button_text == search

def test_recents_button_activation(page: Page) -> None:
    """
    Given I am navigating the org chart
    And I have recent search history
    When I click the previous search button
    Then the search term is entered into the search box
    And the search results are displayed
    """
    searches = ("gvanrossum", "blah",)
    page.goto("http://0.0.0.0:8000/docs/search.html")
    for search in searches:
        page.get_by_label("Search by name").click()
        page.get_by_label("Search by name").fill(search)
        page.get_by_role("button", name="Search").click()
    # activate the button within the recent search history
    page.locator("#previous-searches-list > li > button").click()
    expect(page.locator("#name")).to_have_text("Guido van Rossum")
