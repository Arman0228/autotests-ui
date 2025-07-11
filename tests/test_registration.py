import pytest
from playwright.sync_api import sync_playwright, Page, expect

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):

        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('arman@gmail.com')

        # Заполняем поле Username
        registration_name_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        registration_name_input.fill('arman')

        # Заполняем поле Password
        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Нажимаем на кнопку Registration
        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()