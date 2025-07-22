from playwright.sync_api import sync_playwright, expect



with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('test@gmail.com')

    # Заполняем поле Username
    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill('test')

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

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    #Проверяем наличие Заголовок Courses
    wrong_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(wrong_courses).to_be_visible()
    expect(wrong_courses).to_have_text('Courses')

    #Проверяем иконку "папка"
    wrong_courses_list = page.get_by_test_id('courses-list-empty-view-icon')
    expect(wrong_courses_list).to_be_visible()

    #Проверяем наличие текста There is no results
    wrong_courses_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(wrong_courses_results).to_have_text('There is no results')

    # Проверяем наличие текста Results from the load test pipeline will be displayed here
    wrong_courses_results = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(wrong_courses_results).to_have_text('Results from the load test pipeline will be displayed here')


    page.wait_for_timeout(5000)
