# coding=utf-8
from time import sleep
import unittest
from selenium import webdriver
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *

run_locally = True
#@on_platforms(browsers)

class SmokeTest(unittest.TestCase):

    def test_book_flight_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        book_flight = home_page.header.book_flight()
        book_flight.book_flight_daparture()

        Assert.less_equal(book_flight._first_price, book_flight._second_price)

    def test_tabsfolders_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        book_flight = home_page.header.tabs()
        book_flight.tabsfolderson()

    def test_new_consignment_should_appear_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.check_added_consignment()

        Assert.contains(add_consignment_page._title_uuid, view_consignments_page.get_page_source())
        Assert.contains(u"Polska, Dolnośląskie, Wroclaw, 54-612", view_consignments_page.get_page_source())
        Assert.contains(u'Polska, Mazowieckie, Warszawa, 02-796', view_consignments_page.get_page_source())
        Assert.contains(u'362.70 km', view_consignments_page.get_page_source())
        Assert.contains(u'Tylko transport', view_consignments_page.get_page_source())
        Assert.contains(u'This is my additional info', view_consignments_page.get_page_source())

    def test_add_new_consignment_not_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source())
        Assert.contains(u"Twoje og\u0142oszenie o przesy\u0142ce \xa0zosta\u0142o zapisane, ale musisz si\u0119 <strong>zalogowa\u0107,</strong> aby by\u0142o widoczne dla Przewo\u017anik\xf3w.", add_consignment_page.get_page_source())
        Assert.contains(u"Nie masz konta? <strong>Zarejestruj się </strong><strong>w 1 minutę (za darmo)</strong>. Twoje dane są <strong>chronione</strong> i nie będą upublicznione.", add_consignment_page.get_page_source())
        home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source())

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email, registeration_page.get_page_source())
        Assert.contains(u'Na Twój adres', registeration_page.get_page_source())
        Assert.contains(u'wys\u0142ali\u015bmy e-mail aktywacyjny.\xa0Po aktywacji konta Twoja przesy\u0142ka\xa0zostanie wystawiona.', registeration_page.get_page_source())
        Assert.contains(u'email jest na wp.pl, o2.pl, tlen.pl to sprawdź zakładkę <em>Oferty</em> swojej skrzynki odbiorczej.', registeration_page.get_page_source())

    def test_add_new_consignment_not_logged_in_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source())
        Assert.contains(u"Twoje og\u0142oszenie o przesy\u0142ce \xa0zosta\u0142o zapisane, ale musisz si\u0119 <strong>zalogowa\u0107,</strong> aby by\u0142o widoczne dla Przewo\u017anik\xf3w.", add_consignment_page.get_page_source())
        Assert.contains(u"Nie masz konta? <strong>Zarejestruj się </strong><strong>w 1 minutę (za darmo)</strong>. Twoje dane są <strong>chronione</strong> i nie będą upublicznione.", add_consignment_page.get_page_source())
        home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source())

    def test_register_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email, registeration_page.get_page_source())
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source())

    def test_login_unactivated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.new_user_fill_data()
        account_page = home_page.header.login(registeration_page._username, registeration_page._password)

        Assert.contains(u"Twoja rejestracja nie została ukończona", registeration_page.get_page_source())
        Assert.contains(u"Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.", registeration_page.get_page_source())

    def test_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        home_page.header.login(USER, PASSWORD)
        home_page.header.logout()

        Assert.contains(u"Wylogowałeś się", home_page.get_page_source())

    def test_register_new_transport_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_transport_provider()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source())
        Assert.contains(registeration_page._email, registeration_page.get_page_source())
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source())

    def test_edit_user_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_user_profile()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_edit_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.edit_consignment()
        settings.edit_consignment_move_house()

        Assert.contains(u"Zmiany w Twojej przesyłce", settings.get_page_source())
        Assert.contains(settings._title_uuid, profile_page.get_page_source())
        Assert.contains(u"zostały pomyślnie zapisane.", settings.get_page_source())

    def test_withdraw_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        sleep(3)

        Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source())

    def test_report_violation_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_consignmeent()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        account_page = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_report_violation_to_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.provider_add_question_to_consignment()
        consignment.report_violation_to_question_to_consignment()

        Assert.contains(u"Zgłoszenie zostało odnotowane.", consignment.get_page_source())

    def test_check_categories_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        view_consignment_page = home_page.header.view_consignments_page()
        view_consignment_page.check_categories()
        sleep(10)
        view_consignment_page.click_first_result()
        Assert.contains("Mazowieckie", view_consignment_page.get_page_source())
        Assert.contains('Paczki', view_consignment_page.get_page_source())

    def test_submit_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", submit_offer.get_page_source())

    def test_withdraw_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        profile = home_page.header.open_profile_page()
        profile.withdraw_offer()

        Assert.contains(u"Oferta została wycofana.", profile.get_page_source())

    def test_submit_offer_with_expiration_date_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.submit_offer()
        consignment.enter_expiration_date()
        consignment.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", consignment.get_page_source())

    def test_issue_consignment_again_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        profile = home_page.header.open_profile_page()
        edit_settings = profile.issue_consignment_again()
        edit_settings.edit_consignment_cars()

        Assert.contains(u"Twoja przesyłka", edit_settings.get_page_source())
        Assert.contains(u"została wystawiona!", edit_settings.get_page_source())

    def test_watch_auction_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.watch_consignment()

        Assert.contains(u"Ogłoszenie obserwowane", consignment.get_page_source())

    def test_commission_payback_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page = HomePage(self.driver).open_home_page()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.payback_commission()

        Assert.contains(u"Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.", profile.get_page_source())

    def test_edit_provider_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_profile()

        Assert.contains(u"Profil został zaktualizowany", profile_page.get_page_source())

    def test_edit_provider_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_data()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_edit_provider_notifications_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_notifications()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source())

    def test_change_password_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(CHANGE_PASSWORD_USER, CHANGE_PASSWORD_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.change_password()

        Assert.contains(u"Hasło zostało zmienione.", profile_page.get_page_source())

    def test_reject_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.reject_offer()
        sleep(3)

        Assert.contains(u"Oferta została odrzucona.", consignment.get_page_source())

    def test_add_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        sleep(3)

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my question", consignment.get_page_source())

    def test_provider_reply_to_question_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment=profile.open_first_message()
        consignment.reply_to_question()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my answer", consignment.get_page_source())

    def test_provider_add_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.provider_add_question_to_consignment()

        Assert.contains(u"Twoje pytanie zostało dodane.", consignment.get_page_source())
        Assert.contains(u"This is my question", consignment.get_page_source())

    def test_user_reply_to_question_to_consignment_from_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.user_open_first_message()
        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", consignment.get_page_source())
        Assert.contains(u"This is my reply", consignment.get_page_source())

    def test_accept_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        store = home_page.header.open_profile_page()
        store.store_provider_data()
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        sleep(2)

        Assert.contains("Gratulacje!", consignment.get_page_source())
        Assert.contains(u"Wybrałeś ofertę Przewoźnika <strong>"+PROVIDER_USER, consignment.get_page_source())
        Assert.contains(u"Skontaktuj się z Przewoźnikiem <strong>"+PROVIDER_USER+u"</strong> w celu realizacji usługi transportowej", consignment.get_page_source())
        Assert.contains(u"Imię i nazwisko: <strong>"+store.name1, consignment.get_page_source())
        Assert.contains("tel.: <strong>"+store.tel, consignment.get_page_source())
        Assert.contains("tel. kom.: <strong>"+store.kom, consignment.get_page_source())
        Assert.contains("Nazwa: <strong>"+store.company_name, consignment.get_page_source())
        Assert.contains("e-mail: <strong>"+store.mail, consignment.get_page_source())
        Assert.contains("NIP: <strong>"+store.nip, consignment.get_page_source())
        Assert.contains("REGON: <strong>"+store.regon, consignment.get_page_source())
        Assert.contains(store.address_table[1], consignment.get_page_source())
        Assert.contains(store.address_table[2], consignment.get_page_source())
        Assert.contains(u"Pobierz list przewozowy, który będzie potwierdzeniem nadania Twojej przesyłki", consignment.get_page_source())
        Assert.contains(u"(Ogłoszenie nieaktualne. Użytkownik wybrał już ofertę)", consignment.get_page_source())

    def test_make_offer_executed_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.make_offer_executed()
        sleep(2)

        Assert.contains(u"Oferta ma status zrealizowana.", profile.get_page_source())

    def test_provider_send_commentary_from_my_offers_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_my_offers_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_reply_to_question_to_consignment_from_panel_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        consignment = view_consignments_page.check_added_consignment()
        consignment.provider_add_question_to_consignment()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.user_click_reply_to_question()

        Assert.contains(u"Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika.", profile.get_page_source())

        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", profile.get_page_source())
        Assert.contains(u"This is my reply", profile.get_page_source())

    def test_user_send_commentary_from_ended_transactions_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_ended_transactions_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_user_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_provider_reply_to_negative_commentary_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_negative_commentary()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_reply_to_negative_commentary()

        Assert.contains(u"This is my commentary", profile.get_page_source())
        Assert.contains(u"This is my reply", profile.get_page_source())

    def test_provider_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        submit_offer = view_consignments_page.check_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source())

    def test_ask_for_offer_on_provider_page_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        provider_page = home_page.header.view_provider_lublintransport_page()
        provider_page.ask_for_offer_on_provider_page()

        Assert.contains(u"Twoja prośba o ofertę została wysłana do Przewoźnika.", provider_page.get_page_source())

    def test_ask_for_offer_while_adding_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        add_consignment_page.ask_for_offer_while_adding_consignment()
        sleep(2)

        Assert.contains(u"Prośba wysłana", add_consignment_page.get_page_source())

    def test_ask_for_offer_for_added_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile = home_page.header.open_profile_page()
        profile.ask_for_offer_for_added_consignment()
        sleep(2)
        Assert.contains(u"Prośba wysłana", profile.get_page_source())

    def test_user_add_new_consignment_urgent_and_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_add_new_consignment_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_add_new_consignment_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_login_while_adding_new_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_login_while_adding_new_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(USER, PASSWORD)

        Assert.contains(u"Twoje ogłoszenie zostało zapisane i będzie opublikowane po dokonaniu wpłaty.", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Twoja przesyłka", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)
        Assert.contains(u"została wystawiona! Wyróżnienie ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU.", add_consignment_page.get_page_source())

    def test_user_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited_and_urgent()
        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_after_adding_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited()
        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_user_after_adding_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.user_open_my_consignments_menu()
        profile_page.user_click_first_consignment_distinguish_button()
        profile_page.set_consignment_urgent()
        add_consignment_page.pay_with_test_payment()
        add_consignment_page.get_consignment_title_from_result_page_after_payment()

        Assert.contains(u"Operacja przebiegła pomyślnie. Wyróżnienie Twojego ogłoszenia będzie widoczne od razu po zaksięgowaniu wpłaty w systemie PayU. Zobacz swoje ogłoszenie:", add_consignment_page.get_page_source())
        Assert.equal(add_consignment_page.consignment_title_result_page_after_payment, add_consignment_page._title_uuid)

    def test_provider_add_new_consignment_urgent_and_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_add_new_consignment_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_add_new_consignment_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_highlited()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_login_while_adding_new_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        add_consignment_page.set_urgent()
        add_consignment_page.save_transport()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)

        Assert.contains(u"Twoja przesy\u0142ka zosta\u0142a wystawiona!  Op\u0142ata za wyr\xf3\u017cnienie og\u0142oszenia zosta\u0142a doliczona do Twojego salda (zak\u0142adka Moje konto &gt; Rozliczenia).", add_consignment_page.get_page_source())
        Assert.contains(u"Zalogowałeś się", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_highlited_and_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited_and_urgent()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_highlited_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_highlited()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    def test_provider_after_adding_consignment_set_urgent_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        profile_page = home_page.header.open_profile_page()
        profile_page.provider_open_my_consignments_menu()
        profile_page.provider_click_first_consignment_distinguish_button()
        profile_page.set_consignment_urgent()

        Assert.contains(u"Operacja przebiegła pomyślnie.", add_consignment_page.get_page_source())

    def setUp(self):
        self.timeout = 30

        if run_locally:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(self.timeout)
            # fp = webdriver.ChromeOptions()
            # extension = open("https://crowdworkers.10clouds.com/static/extension_0.2.10.0.crx")
            # fp.add_extension(extension)
            # browser = webdriver.Firefox(firefox_profile=fp)

        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
            self.driver.quit()
        else:
            print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
            try:
                if sys.exc_info() == (None, None, None):
                    sauce.jobs.update_job(self.driver.session_id, passed=True)
                else:
                    sauce.jobs.update_job(self.driver.session_id, passed=False)
            finally:
                self.driver.quit()

if __name__ == '__main__':
     unittest.main()