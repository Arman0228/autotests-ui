from playwright.sync_api import expect, Page
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    """
    Тест проверяет, что:
    1. Отображается заголовок 'Courses'
    2. Видна иконка 'папка'
    3. Отображается текст 'There is no results'
    4. Отображается текст 'Results from the load test pipeline will be displayed here'
    """
    # Используем страницу с сохраненным состоянием из фикстуры
    page = chromium_page_with_state

    # Переходим на страницу курсов
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверяем наличие заголовка 'Courses'
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверяем иконку 'папка'
    empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    # Проверяем текст 'There is no results'
    empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_title).to_have_text('There is no results')

    # Проверяем текст описания
    empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description).to_have_text('Results from the load test pipeline will be displayed here')