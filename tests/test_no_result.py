from playwright.sync_api import Page, expect

def test_exact_heading(page: Page) -> None:
    """
    Check that there is a heading called "Exact match"
    """
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("blah")
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("heading", name="No results found")).to_be_visible()
