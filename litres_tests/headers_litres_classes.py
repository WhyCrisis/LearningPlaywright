from playwright.sync_api import Page
import re

class HeaderPage:
    def __init__(self, page:Page):
        self.page = page
        self.url = "https://www.litres.ru"

        #Логотип
        self.logo = page.get_by_test_id("header--logo")

        #Кнопка каталога
        self.catalog_genres = page.get_by_test_id("header-catalog-button")
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

    def top_search_input(self):
        self.top_search_trigger.click()
        self.top_search_trigger.fill("Энигма")
        self.top_search_find_button.click()