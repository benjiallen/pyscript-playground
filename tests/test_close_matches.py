import pytest
from playwright.sync_api import Page, expect, Locator

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("ben")
    page.get_by_role("button", name="Search").click()
    yield

def test_heading(page: Page) -> None:
    """
    Check that there is a "Close matches" heading
    """
    expect(page.get_by_role("heading", name="Close matches")).to_be_visible()

def test_results_count(page: Page) -> None:
    """
    Check that there is only 1 list and it has 3 items
    """
    results_count = page.locator("li > button").count()
    assert results_count == 3

def test_button_value(page: Page) -> None:
    """
    Check that the first item contains a button with a given value 
    """
    first_result = page.locator("text=benjaminp, Benjamin Peterson")
    expect(first_result).to_have_attribute("value", "benjaminp")

def test_button_activation(page: Page) -> None:
    """
    Check that activating the first button brings up the correct result
    """
    first_result = page.locator("text=benjaminp, Benjamin Peterson")
    first_result.click()
    expect(page.locator("#name")).to_have_text("Benjamin Peterson")
