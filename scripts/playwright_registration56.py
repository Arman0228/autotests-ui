from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('arman@gmail.com')

    # Заполняем поле Username
    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill('arman')

    # Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='../browser-state.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    page.wait_for_timeout(5000)
