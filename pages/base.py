from pages.page import Page

class BasePage(Page):

    _base_url = "http://planaxy.com/"

    @property
    def header(self):
        from pages.regions.header_region import HeaderRegion
        return HeaderRegion(self.get_driver())
