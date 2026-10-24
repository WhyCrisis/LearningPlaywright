from playwright.sync_api import Page, expect


def test_main_page_title(page: Page):
    page.goto("https://modrinth.com/")
    assert page.title() == "Modrinth"

def test_sign_in_page(page: Page):
    page.goto("https://modrinth.com/")
    page.get_by_role("link", name="Sign in").click()
    expect(page).to_have_title("Sign In - Modrinth")