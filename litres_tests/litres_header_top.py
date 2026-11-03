from playwright.sync_api import Page, expect
import re

url= "https://www.litres.ru/"

class TestUp:
    def test_locator_alt_text(self, page:Page):
        page.goto("https://www.litres.ru/popular/")
        page.get_by_alt_text("Логотип Литрес").click()
        expect(page).to_have_url(url)

    def test_catalog_genres(self, page:Page):
        page.goto(url)
        page.get_by_role("button", name="Каталог").click()
        page.get_by_role("link", name=re.compile(r"Все .* жанра")).click()
        expect(page).to_have_url("https://www.litres.ru/pages/new_genres/")

    def test_locator_search(self, page: Page):
        page.goto(url)
        page.get_by_placeholder("Искать на Литрес").fill("Погода")
        page.keyboard.press("Enter")
        expect(page.get_by_text("Результаты поиска «Погода»")).to_be_visible

    def test_bonus_button(self, page:Page):
        page.goto(url)
        page.get_by_role("link", name='Бонусы').click()
        expect(page).to_have_title("Программа лояльности Книголов")

    def test_cart(self, page:Page):
        page.goto(url)
        page.get_by_role("link", name="Корзина").click()
        expect(page).to_have_url("https://www.litres.ru/my-books/cart/")

    def test_my_books(self, page:Page):
        page.goto(url)
        page.get_by_role("link", name="Мои книги").click()


