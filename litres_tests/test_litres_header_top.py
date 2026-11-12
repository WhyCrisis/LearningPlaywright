from playwright.sync_api import expect, Page
from headers_litres_classes import HeaderPage, HeaderCatalogPage
from pathlib import Path
import ast
import pytest

def load_books():
    file_path = Path(__file__).parent / "books.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        return ast.literal_eval(file.read())


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

    @pytest.mark.parametrize("book_name", load_books())
    def test_locator(self, header: HeaderPage, book_name: str, page: Page):
        header.open()
        header.top_search_input(book_name)
        expect(page.get_by_test_id("search-title__wrapper")).to_contain_text(f"Результаты поиска «{book_name}»")
        print(f"\nКнига '{book_name}' найдена")

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


#Временные проверки выполняемые вне теста
    def test_check_title_box(self, header: HeaderPage):
        header.open()
        header.catalog_genres.click()
        (header.use(HeaderCatalogPage)
            .wait_catalog_menu_opened()
            .expected_genres_count(19)
            .verify_columns_structure())