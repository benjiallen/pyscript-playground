"""
## Scenario: search by handle with exact and close matches

Search "benjaminp"
Expect "exact match" and "close matches" heading
Check details of exact match
Check the number of close matches

## Scenario: activate manager button

Search "benjaminp"
Expect "manager" heading
Activate the first button
Expect an exact match, check details of matc

## Scenario: activate reports button

Search "benjaminp"
Expect "reports" heading
Activate the first button
Expect an exact match, check details of match
"""
import pytest
from playwright.sync_api import Page, expect, Locator

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("http://0.0.0.0:8000/docs/org-chart.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("benjaminp")
    page.get_by_role("button", name="Search").click()
    yield

def test_exact_heading(page: Page) -> None:
    """
    Check that there is a heading called "Exact match"
    """
    heading: Locator = page.locator("#exact-match-heading")
    expect(heading).to_have_text("Exact match")

def test_close_heading(page: Page) -> None:
    """
    Check that there is a heading called "Close matches"
    """
    heading: Locator = page.get_by_role("heading", name="Close matches")
    expect(heading).to_be_visible()

def test_details_of_exact_match(page: Page) -> None:
    """
    Check that the exact match details are correct
    """
    expect(page.locator("#name")).to_have_text("Benjamin Peterson")
    expect(page.locator("#title")).to_have_text("Product Manager")
    expect(page.locator("#email")).to_have_text("No email available")
    expect(page.locator("#cost-center")).to_have_text("No cost center available")
    expect(page.locator("#country")).to_have_text("No country available")
    expect(page.locator("#employment-type")).to_have_text("employee")
    expect(page.locator("#manager button")).to_have_text("gvanrossum, Guido van Rossum")

def test_close_results_count(page: Page) -> None:
    """
    Check that there is only 1 "close match" list and it has 2 items
    """
    results_count = page.locator("#close-match-result > ul > li").count()
    assert results_count == 2

def test_manager_button_activation(page: Page) -> None:
    """
    Check that activating the first button brings up the correct result
    """
    page.locator("text=gvanrossum, Guido van Rossum").click()
    expect(page.locator("#name")).to_have_text("Guido van Rossum")

def test_reports_heading_is_visible(page: Page) -> None:
    """
    Check that the reports heading is visible
    """
    expect(page.get_by_role("heading", name="Reports")).to_be_visible()

def test_reports_results_count(page: Page) -> None:
    """
    Check that there is only 1 "reports" list and it has 10 items
    """
    results_count = page.locator("#reports > ol > li").count()
    assert results_count == 10

def test_reports_button_activation(page: Page) -> None:
    """
    Check that activating the first button brings up the correct result
    """
    page.locator("text=erlend-aasland, Erlend E. Aasland").click()
    expect(page.locator("#name")).to_have_text("Erlend E. Aasland")
