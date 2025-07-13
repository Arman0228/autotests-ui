from pages.base_page import BasePage
from playwright.sync_api import expect


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Локатор заголовка Dashboard
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def is_dashboard_title_visible(self):
        """
        Проверяет видимость заголовка Dashboard
        :return: None (вызывает assertion)
        """
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text("Dashboard")

