from playwright.sync_api import Page, expect, Locator


def test_example(page: Page) -> None:

    page.goto("http://0.0.0.0:8000/docs/org-chart.html")

    page.get_by_label("Search by name").click()

    page.get_by_label("Search by name").fill("ben")

    page.get_by_role("button", name="Search").click()

    heading: Locator = page.get_by_role("heading", name="Close matches")

    expect(heading).to_be_visible()
