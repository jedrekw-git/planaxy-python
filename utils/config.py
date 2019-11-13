import os
from sauceclient import SauceClient

USERNAME = os.environ.get('SAUCE_USERNAME', "testuj")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0029898f-54be-48b2-9166-9306282bef0c")
sauce = SauceClient(USERNAME, ACCESS_KEY)

USER = "testujpl"
PASSWORD = "paluch88"

PROVIDER2_USER = "lublintransport"
PROVIDER2_PASSWORD = "TestoojemyClick"

PROVIDER_USER = "JLMTranspol"
PROVIDER_PASSWORD = "TestoojemyClick"

CHANGE_PASSWORD_USER = "testujgo2"
CHANGE_PASSWORD_PASSWORD = "paluch88"

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "firefox",
#              "version": "33"}]

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "internet explorer",
#              "version": "11"}]

browsers = [{"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "8"},
            {"platform": "Windows 8.1",
             "browserName": "firefox",
             "version": "35"}]

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "chrome",
#              "version": "31"},
#             {"platform": "Windows 8.1",
#              "browserName": "internet explorer",
#              "version": "11"},
#             {"platform": "Windows 8.1",
#              "browserName": "firefox",
#              "version": "33"}]