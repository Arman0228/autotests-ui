from typing import Any, Generator

import pytest  # Импортируем pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:  # Аннотируем возвращаемое фикстурой значение
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, args=["--ignore-certificate-errors"])
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(
        email='username@gmail.com', username='username', password='password'
    )
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, args=["--ignore-certificate-errors"])
    context = browser.new_context(
        storage_state="browser-state.json",
        ignore_https_errors=True
    )
    page = context.new_page()
    yield page
    context.close()
    browser.close()