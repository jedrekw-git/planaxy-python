from selenium.webdriver.common.by import By
from pages.add_consignment import AddConsignmentPage
from pages.page import Page



class HeaderRegion(Page):
    _login_field = (By.NAME, "login")
    _password_field = (By.NAME, "password")
    _login_button = (By.XPATH, "//input[@value='Zaloguj']")
    _base_url = "http://planaxy.com/"
    _url_tabsfolders = "https://www.tabsfolders.com/"
    _url_crowdworkers = "http://crowd-workers.com/landing"
    _logout_button = (By.XPATH, "/html/body/div[1]/div[1]/div/ul/li[3]/a")
    _continue_to_registration_page_button = (By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[5]/div/a")

    def login(self, login, password):
        self.get(self._base_url + "logowanie,pid,2.html")
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)

    def logout(self):
        self.click(self._logout_button)

    def book_flight(self):
        self.get(self._base_url + "wyszukaj-transport")
        return AddConsignmentPage(self.get_driver())

    def tabs(self):
        self.get(self._url_crowdworkers)
        return AddConsignmentPage(self.get_driver())

    def view_consignments_page(self):
        self.get(self._base_url + "przegladaj-przesylki/?resetfilters=1")
        return ViewConsignmentsPage(self.get_driver())

    def open_registration_page(self):
        self.get(self._base_url + "rejestracja,pid,3.html")
        return RegistrationPage(self.get_driver())

    def open_profile_page(self):
        self.get(self._base_url + "moje-konto,pid,6.html")
        return ProfilePage(self.get_driver())

    def view_provider_lublintransport_page(self):
        self.get(self._base_url + "firmy-transportowe/lublintransport.html")
        return ProviderPage(self.get_driver())

    def continue_to_registration_page(self):
        self.click(self._continue_to_registration_page_button)
        return RegistrationPage(self.get_driver())