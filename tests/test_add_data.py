import pytest
from playwright.sync_api import Page, expect, Locator

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("http://0.0.0.0:8000/docs/add.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("ben")
    page.get_by_role("button", name="Add data").click()
    yield

@pytest.mark.skip(reason="not implemented yet")
def test_success_message_present(page: Page) -> None:
    """
    Scenario: user uploads a file and a success message is displayed

    When I select a file
    And I click the "Add data" button
    Then I should see a success message
    """

@pytest.mark.skip(reason="not implemented yet")
def test_data_stored_in_localstorage(page: Page) -> None:
    """
    Scenario: user uploads a file and the contents is stored to localstorage

    When I select a file
    And I click the "Add data" button
    Then the contents of the file should be stored in localstorage
    """

@pytest.mark.skip(reason="not implemented yet")
def test_search_new_data(page: Page) -> None:
    """
    Scenario: the data stored in localstorage is searchable

    Given I have added an org chart file
    When I navigate to the search page
    And I enter a name in the search box
    Then I will get the correct results
    """
