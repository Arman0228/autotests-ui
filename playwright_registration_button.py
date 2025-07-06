from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    # Проверяем на то, что Registration отключена
    expect(registration_button).to_be_disabled()

    #Заполняем поле Email
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    #Заполняем поле Username
    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill('username')

    # Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    # Проверяем на то, что Registration включена
    expect(registration_button).not_to_be_disabled()
    # Добавляем паузу для наглядности результата
    page.wait_for_timeout(5000)