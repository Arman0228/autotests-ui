from typing import Any, Generator

import pytest  # Импортируем pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:  # Аннотируем возвращаемое фикстурой значение
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('username@gmail.com')

    # Заполняем поле Username
    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill('username')

    # Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранение состояния
    context.storage_state(path='browser-state.json')
    #Закрытие браузера
    context.close()
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    """Фикстура для создания страницы с сохраненным состоянием браузера"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page

    # Очистка после теста
    context.close()
    browser.close()