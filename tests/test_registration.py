import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize("email,username,password", [
    ("test1@example.com", "user1", "Password123!"),
    ("test2@example.com", "user2", "SecurePass456!")
])
def test_successful_registration(registration_page, dashboard_page, email, username, password, request):
    """
    Параметризованный тест успешной регистрации
    с правильными ожиданиями и возможностью визуальной проверки
    """
    # 1. Заполнение формы регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form_email_input(email)
    registration_page.fill_registration_form_username_input(username)
    registration_page.fill_registration_form_password_input(password)

    # 2. Отправка формы
    registration_page.click_registration_form_submit_button()

    # 3. Явное ожидание перехода на Dashboard
    dashboard_page.page.wait_for_url("**/dashboard", timeout=15000)

    # 4. Проверка элементов Dashboard
    dashboard_page.is_dashboard_title_visible()

    # 5. Скриншот для документации
    dashboard_page.page.screenshot(path=f"results/{request.node.name}.png", full_page=True)

    # 5. Дополнительно: скриншот для документации
    dashboard_page.page.screenshot(path=f"screenshot_{username}.png", full_page=True)