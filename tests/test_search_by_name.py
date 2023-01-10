"""
## Scenario: search by name with spaces

Search "brian curtin"

## Scenario: search by duplicate name

Search "Guido van Rossum"
expect "employees with same name" heading

## Scenario: search by start of duplicate name

Search "guido"
expect only close matches
"""
import pytest
from playwright.sync_api import Page, expect, Locator

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    yield

def test_name_with_exact_match(page: Page) -> None:
    """
    Search "brian curtin"
    Expect the result to be "Brian Curtin"
    """
    page.get_by_label("Search by name").fill("brian curtin")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("#name")).to_have_text("Brian Curtin")

def test_name_with_duplicate_matches(page: Page) -> None:
    """
    Search "Guido van Rossum"
    Expect "Employees with the same name" heading
    """
    page.get_by_label("Search by name").fill("Guido van Rossum")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("h2")).to_have_text("Employees with the same name")

def test_name_with_close_matches(page: Page) -> None:
    """
    Search "guido"
    Expect "Close matches" heading
    """
    page.get_by_label("Search by name").fill("guido")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("h2")).to_have_text("Close matches")
