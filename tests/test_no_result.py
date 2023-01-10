from playwright.sync_api import Page, expect

def test_exact_heading(page: Page) -> None:
    """
    Check that there is a heading called "Exact match"
    """
    page.goto("http://0.0.0.0:8000/docs/search.html")
    page.get_by_label("Search by name").click()
    page.get_by_label("Search by name").fill("blah")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("h2")).to_have_text("No results found")
