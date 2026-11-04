from playwright.sync_api import Page, expect
import re

class HeaderPage:
    def __init__(self, page:Page):
        self.page = page
        self.url = "https://www.litres.ru/"

        #Логотип
        self.logo = page.get_by_test_id("header--logo")

        #Кнопка каталога
        self.catalog_genres = page.get_by_test_id("header-catalog-button")
        self.genres_genres = page.get_by_role("link", name=re.compile(r"Все .* жанра"))

        #Поисковик
        self.top_search = page.get_by_test_id("search__input")
        self.top_search_find_button = page.get_by_test_id("search__button")

        #Пользовательские разделы
        self.bonus_button = page.get_by_role("link", name = "Бонусы")
        self.cart_button = page.get_by_role("link", name = "Корзина")
        self.mybooks_button = page.get_by_role("link", name = "Мои книги")
        self.login_button = page.get_by_role("link", name = "Войти")

    def open(self):
        self.page.goto(self.url)
