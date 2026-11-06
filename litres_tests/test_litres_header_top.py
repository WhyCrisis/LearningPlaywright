from playwright.sync_api import Page, expect
import re
from headers_litres_classes import HeaderPage


class TestHeaderBar:

    def test_logo(self, page: Page):
        b = HeaderPage(page)
        #Действия
        b.open("/popular/")
        b.logo.click()
        #Проверка
        expect(page).to_have_url("https://www.litres.ru/")

    def test_catalog(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.catalog_genres.click()
        b.catalog_genres_all.click()

        expect(page).to_have_url("https://www.litres.ru/pages/new_genres/")

    def test_locator(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.top_search.click()
        b.top_search_input()

        expect(page.get_by_text("Результаты поиска «Энигма»")).to_be_visible()

    def test_bonus_button(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.bonus_button.click()

        expect(page).to_have_title("Программа лояльности Книголов")

    def test_cart_button(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.cart_button.click()

        expect(page).to_have_url("https://www.litres.ru/my-books/cart/")

    def test_my_books_button(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.mybooks_button.click()

        expect(page.get_by_text("Мои", exact=True)).to_be_visible()
        expect(page.get_by_text("Отложено")).to_be_visible()
        expect(page.get_by_text("Списки")).to_be_visible()
        expect(page.get_by_text("Я слежу")).to_be_visible()

    def test_login_button(self, page: Page):
        b = HeaderPage(page)
        b.open()
        b.login_button.click()

        expect(page.get_by_test_id("auth__title")).to_be_visible()


