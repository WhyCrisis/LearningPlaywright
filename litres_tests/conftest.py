import pytest
from playwright.sync_api import Page
from headers_litres_classes import HeaderPage

@pytest.fixture
def header(page: Page):
    return HeaderPage(page)
