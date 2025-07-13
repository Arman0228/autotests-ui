from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Основные элементы формы
        self.registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_submit_button = page.get_by_test_id('registration-page-registration-button')

        # Элементы для валидации
        self.email_error = page.get_by_test_id('registration-form-email-error-alert')
        self.username_error = page.get_by_test_id('registration-form-username-error-alert')
        self.password_error = page.get_by_test_id('registration-form-password-error-alert')

        # Ссылки
        self.login_link = page.get_by_test_id('registration-page-login-link')



    def fill_registration_form_email_input(self, email: str):
        self.registration_email_input.fill(email)
        expect(self.registration_email_input).to_have_value(email)

    def fill_registration_form_username_input(self, username: str):
        self.registration_username_input.fill(username)
        expect(self.registration_username_input).to_have_value(username)

    def fill_registration_form_password_input(self, password: str):
        self.registration_password_input.fill(password)
        expect(self.registration_password_input).to_have_value(password)

    def click_registration_form_submit_button(self):
        self.registration_submit_button.click()

