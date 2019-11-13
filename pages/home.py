# coding=utf-8
from pages.base import BasePage


class HomePage(BasePage):
    _title = "planaxy"
    _url_planaxy = "http://planaxy.com/"
    _url = "https://www.tabsfolders.com/"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver, self._title, self._url)

    def open_home_page(self):
        self.get(self._url)
        self.is_the_current_page()
        return self