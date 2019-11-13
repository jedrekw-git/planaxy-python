import requests
from config import USER, PASSWORD



class Api():
    def __init__(self, credentials=None):
        if not credentials:
            self.credentials = {"email": USER, "password": PASSWORD}
        self.url = "http://klaudia:firekklaudia015@klaudiajson.aftermarket.pl/"

    def get_contact_list(self):
        return self.make_get_request("contact/list")

    def add_contact(self, contact):
        data = {
            "pname": contact.pname,
            "fname": contact.fname,
            "lname": contact.lname,
            "address": contact.address,
            "city": contact.city,
            "email2": contact.email2,
            "country": contact.country,
            "zip": contact.zip,
            "phone": contact.phone
        }

        return self.make_post_request("contact/add", data)

    def remove_contact(self, contact):
        data = {
            "contact_id": contact.id
        }

        return self.make_post_request("contact/remove", data)

    def register_account(self, account):
        data = {
            "accountEmail": account.email,
            "accountPassword": account.password,
            "city": account.city,
            "firstName": account.first_name,
            "lastName": account.last_name,
            "phone": account.phone,
            "street": account.street,
            "zip": account.zip
        }

        return self.make_post_request("account/register", data)

    def make_get_request(self, method):
        return requests.get(
            self.url + method,
            params=self.credentials,
            headers={'User-Agent': 'Mozilla/5.0'}
        ).json()

    def make_post_request(self, method, data):
        return requests.post(
            self.url + method,
            data=dict(self.credentials, **data),
            headers={'User-Agent': 'Mozilla/5.0'}
        ).json()

