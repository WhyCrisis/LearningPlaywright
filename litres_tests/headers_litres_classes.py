from playwright.sync_api import Page, expect
import re

class HeaderPage:
    def __init__(self, page:Page):
        self.page = page
        self.url = "https://www.litres.ru"

        #Логотип
        self.logo = page.get_by_test_id("header--logo")

        #Кнопка каталога
        self.catalog_genres = page.get_by_test_id("header-catalog-button")
        self.catalog_close_button = page.get_by_test_id("icon_close")
        self.catalog_genres_all = page.get_by_role("link", name=re.compile(r"Все .* жанра"))

        #Поисковик
        self.top_search_trigger = page.get_by_test_id("search__input")
        self.top_search_find_button = page.get_by_test_id("search__button")
        self.find_page = page.get_by_test_id("search-title__wrapper")

        #Пользовательские разделы
        self.bonus_button = page.get_by_role("link", name = "Бонусы")
        self.cart_button = page.get_by_role("link", name = "Корзина")
        self.mybooks_button = page.get_by_role("link", name = "Мои книги")
        self.login_button = page.get_by_role("link", name = "Войти")

    def open(self, path: str = "/"):
        self.page.goto(f"{self.url}{path}")

    def top_search_input(self, book_name: str):
        self.top_search_trigger.click()
        self.top_search_trigger.fill(book_name)
        self.top_search_find_button.click()

    def use(self, component_class):
        return component_class(self.page)
class HeaderCatalogPage:
    def __init__(self, page:Page):
        self.scope = page.get_by_test_id ("popup__genreContainer--wrapper")
        self.columns = self.scope.locator(".yCj_CG_column")

    def wait_catalog_menu_opened(self):
        expect(self.scope).to_be_visible(timeout=7000)
        return self
    
    def verify_columns_structure(self):
        all_columns = self.columns.all()
        assert len(all_columns) > 0, "Columns not found!"

        for column in all_columns:
            expect(column).to_be_visible()
            title = (column).get_by_test_id("popup__genreTitle")

            expect(title).to_be_visible()
            expect(title).not_to_be_empty()
            expect(title).to_have_attribute("href", re.compile(r"^/.+/$"))
        return self


    def expected_genres_count(self, expected_count: int):
        expect(self.columns).to_have_count(expected_count)
        return self

