# coding=utf-8
import unittest
from selenium import webdriver
from unittestzero import Assert
from pages.home import HomePage
from utils.utils import *
from utils.config import *



run_locally = False

# it's best to remove the hardcoded defaults and always get these values
# from environment variables
# USERNAME = os.environ.get('SAUCE_USERNAME', "clicktrans")
# ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "88a7db15-e558-413f-b55d-288e883ff00c")
USERNAME = os.environ.get('SAUCE_USERNAME', "testuj")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0029898f-54be-48b2-9166-9306282bef0c")
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Windows 8",
             "browserName": "firefox",
             "version": "35.0"}]

def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)

    return decorator

@on_platforms(browsers)
class SmokeTest(unittest.TestCase):

    #ABY URUCHOMIC TESTY NA SAUCELABS'IE PRZENIEŚ TUTAJ SKRYPT KTÓRY CHCESZ WYKONAC Z PLIKU test.py Z FOLDERU tests np.
    # I URUCHAMIAJ KLIKAJĄC PRAWYM KLAWISZEM NA def on_platforms(platforms): I KLIKAJĄC Run 'Unittests in saucelabs'

    def test_book_flight_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        book_flight = home_page.header.book_flight()
        book_flight.book_flight_daparture()

        Assert.less_equal(book_flight._first_price, book_flight._second_price)

    def setUp(self):
        self.timeout = 30

        if run_locally:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(self.timeout)
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