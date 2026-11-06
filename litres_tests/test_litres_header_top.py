from playwright.sync_api import expect, Page
from headers_litres_classes import HeaderPage

class TestHeaderBar:

    def test_logo(self, header: HeaderPage, page: Page):
        header.open("/popular/")
        header.logo.click()
        #Проверка
        expect(page).to_have_url("https://www.litres.ru/")

    def test_catalog(self, header: HeaderPage, page: Page):
        header.open()
        header.catalog_genres.click()
        header.catalog_genres_all.click()
        #Проверка
        expect(page).to_have_url("https://www.litres.ru/pages/new_genres/")

    def test_locator(self, header: HeaderPage, page: Page):
        header.open()
        header.top_search_input()
        #Проверка
        expect(page.get_by_text("Результаты поиска «Энигма»")).to_be_visible()

    def test_bonus_button(self, header: HeaderPage, page: Page):
        header.open()
        header.bonus_button.click()
        #Проверка
        expect(page).to_have_title("Программа лояльности Книголов")

    def test_cart_button(self, header: HeaderPage, page: Page):
        header.open()
        header.cart_button.click()
        #Проверка
        expect(page).to_have_url("https://www.litres.ru/my-books/cart/")

    def test_my_books_button(self, header: HeaderPage, page: Page):
        header.open()
        header.mybooks_button.click()
        #Проверки
        expect(page.get_by_text("Мои", exact=True)).to_be_visible()
        expect(page.get_by_text("Отложено")).to_be_visible()
        expect(page.get_by_text("Списки")).to_be_visible()
        expect(page.get_by_text("Я слежу")).to_be_visible()

    def test_login_button(self, header: HeaderPage, page: Page):
        header.open()
        header.login_button.click()
        #Проверка
        expect(page.get_by_test_id("auth__title")).to_be_visible()


