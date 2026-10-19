from playwright.async_api import async_playwright
import asyncio

async def main(window):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not window)
        page = await browser.new_page()
        await page.goto("https://support.microsoft.com/ru-ru/windows/security/firewall/risks-of-allowing-apps-through-windows-firewall#:~:text=There%20are%20two%20ways%20to%20allow%20an%20app,though%20you%20drilled%20a%20hole%20in%20the%20firewall.")
        await page.screenshot(path="microsoft.png")
        await browser.close()

print("Wanna see window?: y/n")
window_open = input("")

if window_open == 'y':
    window = True
    asyncio.run(main(window))

if window_open == 'n':
    window = False
    asyncio.run(main(window))
    print("screenshot was taken!")
