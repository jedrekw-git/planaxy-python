# coding=utf-8
from selenium.webdriver.common.by import By
import datetime
from time import sleep
from utils.utils import *
from pages.base import BasePage
from pages.page import *
from selenium.webdriver.support.expected_conditions import *


class AddConsignmentPage(BasePage):

    _title = "Add consignment"
    _url = "http://planaxy.com/"

    _departure_city_field = (By.XPATH, "/html/body/section[1]/div/form/fieldset/div[1]/div[1]/div[2]/div[1]/span/input[2]")
    _departure_first_element_dropdown = (By.XPATH, "html/body/section[1]/div/form/fieldset/div[1]/div[1]/div[2]/div[1]/span/span/div/span/div[1]/p")
    _departure_date_field = (By.CLASS_NAME, "field--date--icon")
    _departure_date = (By.CLASS_NAME, "ui-datepicker-today")
    _arrival_city_field = (By.XPATH, "(//input[@id='id_place_02'])[2]")
    _arrival_first_element_dropdown = (By.XPATH, "html/body/section[1]/div/form/fieldset/div[1]/div[2]/div[1]/div[1]/span/span/div/span/div[1]/p")
    _arrival_date_field = (By.XPATH, "//div[2]/div/div[2]/span")
    _arrival_date = (By.LINK_TEXT, str(datetime.date.today().day+2))
    _search_transport_submit = (By.XPATH, "/html/body/section[1]/div/form/fieldset/div[2]/div[2]/button")
    _filter_button = (By.XPATH, "/html/body/section[1]/div/div[2]/div[1]/fieldset/form[1]/div[2]/div[5]/button")
    _first_price_path = (By.XPATH, "/html/body/section[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/strong/span")
    _second_price_path = (By.XPATH, "/html/body/section[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/strong/span")

    _third_tab = (By.XPATH, "/html/body/div[1]/section/div/div[2]/div[2]/div[1]/div/ul/li/ul/li/ul/li[3]/a")
    _rozwin_home = (By.XPATH, "/html/body/div[1]/section/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/i")
    _rozwin_folder1 = (By.CSS_SELECTOR, "html.logged-in.tabsfolder-ext.firefox-browser.windows-os.gecko-engine body.tabs.page-item div#main.container-fluid.panel section div#navigatePanels div.a-panel.active div.a-body.nano.has-scrollbar div.nano-content div#jsTree.jstree.jstree-1.jstree-tf ul.jstree-container-ul.jstree-children.jstree-striped.jstree-wholerow-ul.jstree-no-dots li#f#.jstree-node.root-item.jstree-open.jstree-last ul.jstree-children li#f1041fqn.jstree-node.dir-item.jstree-last.jstree-closed i.jstree-icon.jstree-ocl")
    _email_facebook = (By.ID, "email")
    _pass_facebook = (By.ID, "pass")
    _facebook_log_in = (By.ID, "u_0_2")
    _fblogin_button = (By.NAME, "fblogin")
    _facebook_confirm = (By.NAME, "__CONFIRM__")
    _no_promo = (By.LINK_TEXT, "No Promo")
    _set_price_and_deadline = (By.XPATH, "//input[@value='Podaj trasę i termin']")
    _add_extension_crowdworker = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div")

    def __init__(self, driver):
        super(AddConsignmentPage, self).__init__(driver, self._title)

    def book_flight_daparture(self):
        self.clear_field_and_send_keys("Radom", self._departure_city_field)
        self.click(self._departure_first_element_dropdown)
        self.click(self._departure_date_field)
        self.click(self._departure_date)
        self.clear_field_and_send_keys("Madrid", self._arrival_city_field)
        self.click(self._arrival_first_element_dropdown)
        self.click(self._arrival_date_field)
        self.click(self._arrival_date)
        self.click(self._search_transport_submit)
        self.wait_for_visibility(self._filter_button, 20)
        self._first_price = self.get_text(self._first_price_path)
        self._second_price = self.get_text(self._second_price_path)

    def tabsfolderson(self):
        sleep(10)
        self.switch_window()
        self.clear_field_and_send_keys("testujpl@o2.pl", self._email_facebook)
        self.clear_field_and_send_keys("paluch88", self._pass_facebook)
        self.click(self._facebook_log_in)
        click_element_if_visible(self._facebook_confirm)
        click_element_if_visible(self._no_promo)
        sleep(10)
        # self.click(self._rozwin_home)
        self.click(self._rozwin_folder1)
        self.click(self._third_tab)

    def crowdworker(self):
        self.click(self._add_extension_crowdworker)

    def new_furniture_consignment(self):
        self.click(self._send_date_from_field)
        self.click(self._send_date_from)
        self.click(self._send_date_to_field)
        self.click(self._send_date_to)
        return self._title_uuid

    def edit_consignment_move_house(self):
        self.click(self._home_removal_link)
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title)
        self.select_index_from_dropdown(2, self._moving_type_of_service_dropdown)
        self.select_index_from_dropdown(2, self._type_of_house)
        self.select_index_from_dropdown(2, self._number_of_rooms)
        self.clear_field_and_send_keys(2, self._departure_floor)
        self.clear_field_and_send_keys(2, self._destination_floor)
        self.clear_field_and_send_keys(get_random_integer(2), self._weight)
        self.clear_field_and_send_keys(250, self._removal_budget)
        self.clear_field_and_send_keys(get_random_string(20), self._additional_info)
        self.click(self._set_price_and_deadline)
        self.select_index_from_dropdown(2, self._send_province_dropdown)
        self.clear_field_and_send_keys("Breslau", self._send_city)
        self.clear_field_and_send_keys("54-699", self._send_post_code)
        self.select_index_from_dropdown(3, self._receive_province)
        self.clear_field_and_send_keys("Poznan", self._receive_city)
        self.clear_field_and_send_keys("65-600", self._receive_post_code)
        self.select_index_from_dropdown(1, self._period)
        self.click(self._save_edit_consignment)

    def get_consignment_title_from_result_page(self):
        self.consignment_title_result_page = self.get_text(self._consignment_title_result_page)

    def get_consignment_title_from_result_page_after_payment(self):
        self.consignment_title_result_page_after_payment = self.get_text(self._consignment_title_result_page_after_payment)

    def edit_consignment_cars(self):
        self.click(self._cars_link)
        sleep(2)
        self.clear_field_and_send_keys("Pontiac 100", self._car_model)
        self.clear_field_and_send_keys(get_random_integer(2), self._car_weight)
        self.clear_field_and_send_keys(get_random_integer(3), self._car_budget)
        self.clear_field_and_send_keys(get_random_string(20), self._additional_info)
        self.click(self._set_price_and_deadline)
        self.select_index_from_dropdown(4, self._send_province_dropdown)
        self.clear_field_and_send_keys("Edited", self._send_city)
        self.clear_field_and_send_keys("50-690", self._send_post_code)
        self.select_index_from_dropdown(5, self._receive_province)
        self.clear_field_and_send_keys("Also", self._receive_city)
        self.clear_field_and_send_keys("05-880", self._receive_post_code)
        self.select_index_from_dropdown(2, self._period)
        self.click(self._save_transport_button)

    def ask_for_offer_while_adding_consignment(self):
        self.click(self._first_offer)

    def add_consignment_parcel(self):
        self.click(self._parcel_link)
        sleep(2)
        self.send_keys(self._title_uuid, self._consignment_title)
        self.clear_field_and_send_keys("3", self._consignment_length)
        self.clear_field_and_send_keys("4", self._consignment_width)
        self.clear_field_and_send_keys("2", self._consignment_height)
        self.clear_field_and_send_keys("15", self._consignment_weight)
        self.clear_field_and_send_keys("5", self._quantity)
        self.clear_field_and_send_keys("This is my additional info", self._additional_info)
        self.click(self._set_price_and_deadline)
        self.select_index_from_dropdown(1, self._send_province_dropdown)
        self.send_keys("Wroclaw", self._send_city)
        self.clear_field_and_send_keys("54-612", self._send_post_code)
        self.select_index_from_dropdown(2, self._receive_province)
        self.send_keys("Warszawa", self._receive_city)
        self.send_keys("65-634", self._receive_post_code)
        self.click(self._send_date_from_field)
        self.click(self._send_date_from)
        self.click(self._send_date_to_field)
        self.click(self._send_date_to)
        self.click(self._receive_date_from_field)
        self.click(self._receive_date_from)
        self.click(self._receive_date_to_field)
        self.click(self._receive_date_to)
        self.select_index_from_dropdown(2, self._period)

    def set_highlited(self):
        self.check(self._highlited_checkbox)

    def set_urgent(self):
        self.click(self._urgent_checkbox)

    def save_transport(self):
        self.click(self._save_transport_button)

    def pay_with_test_payment(self):
        self.click(self._test_payment_radio)
        self.select_index_from_dropdown(get_random_integer(2), self._invoice_company_country)
        self.click(self._submit_payment_button)
        self.click(self._payu_accept_button)
        self.click(self._payu_valid_authorization)