from playwright.sync_api import Locator

from elements.base_element import BaseElement


class Textarea(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('texterea').first


