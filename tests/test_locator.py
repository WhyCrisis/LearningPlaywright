from playwright.sync_api import Page, expect

def test_locator_role(page: Page):  
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name="С чего начать").click()
    expect(page).to_have_title("Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres")
    page.get_by_role("button", name = "Найти").click()
    expect(page.get_by_text("лина коваль")).to_be_visible()

def test_locator_placeholder(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("матрица судьбы")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «матрица судьбы»"))

def test_locator_dataid(page:Page):
    page.goto("https://www.litres.ru/")
    page.get_by_test_id("header--logo").click()
    expect(page.get_by_text("С чего начать")).to_be_visible()

def test_locator_alt_text(page:Page):
        page.goto("https://www.litres.ru/popular/")
        page.get_by_alt_text("Логотип Литрес").click()
        expect(page).to_have_url("https://www.litres.ru/")

def test_locator_xpath(page:Page):
    page.goto("https://www.litres.ru/")
    expect(page.locator("xpath=//a[@title='ВКонтакте']")).to_be_visible()
