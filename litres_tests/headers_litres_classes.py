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

        #Пользовательские разделы
        self.bonus_button = page.get_by_role("link", name = "Бонусы")
        self.cart_button = page.get_by_role("link", name = "Корзина")
        self.mybooks_button = page.get_by_role("link", name = "Мои книги")
        self.login_button = page.get_by_role("link", name = "Войти")

    def open(self, path: str = "/"):
        self.page.goto(f"{self.url}{path}")

    def use(self, component_class):
        return component_class(self.page)

    
    def top_search_input(self):
        self.top_search_trigger.click()
        self.top_search_trigger.fill("Энигма")
        self.top_search_find_button.click()

class HeaderCatalogPage:
    def __init__(self, page:Page):
        self.scope = page.get_by_test_id ("popup__genreContainer--wrapper")

        #проверка содержимого контейнера
        self.all_genres_title = self.scope.locator(".yCj_CG_column")

    def wait_catalog_menu_opened(self):
        expect(self.scope).to_be_visible(timeout=5000)
        return self
    
    def expected_genres_count(self, expected_count: int):
        expect(self.all_genres_title).to_have_count(expected_count)
        return self

