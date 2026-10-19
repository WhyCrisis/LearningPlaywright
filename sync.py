from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page: Page = browser.new_page()
    page.goto("https://www.gismeteo.ru/weather-stavropol-5141/")
    page.screenshot(path="pogoda.png")
    browser.close