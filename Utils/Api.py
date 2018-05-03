import json
import requests


class BaseAPI():
    def __init__(self):
        self.main_url = "http://localhost:5000/v1"
        self.token_url = self.main_url + "/token"
        self.cars_url = self.main_url + "/cars"

    def get_auth_token(self, data=None):
        auth_token = None
        response = requests.post(self.token_url, json=data)
        return response

    def delete_car(self, car_id, auth_token):
        delete_url = "%s/%s" % (self.cars_url, car_id)
        response = requests.delete(url=delete_url, headers={'auth_token': auth_token})
        return response

    def retrieve_car_details(self, auth_token):
        response = requests.get(url=self.cars_url, headers={'auth_token': auth_token})
        return response

    def add_a_new_car(self, brand_name, model_name, power_rating, daily_price, auth_token):
        new_car_details = {'brand': brand_name, 'model': model_name, 'power_rating': power_rating,
                           'daily_price': daily_price}
        headers = {'content-type': 'application/json', 'auth_token': auth_token}
        response = requests.post(self.cars_url, data=json.dumps(new_car_details), headers=headers)
        return response


class APITestWrapper(BaseAPI):
    def add_new_car(self, brand=None, model=None, power_rating=None, daily_price=None, auth_token=None):
        if brand is None:
            brand = "model"
        if model is None:
            model = "brand"
        if power_rating is None:
            power_rating = 1
        if daily_price is None:
            daily_price = 1
        if auth_token is None:
            auth_token = self.fetch_token(scope="W").json().get("auth_token")
        return self.add_a_new_car(brand, model, power_rating, daily_price, auth_token)

    def fetch_token(self, client_id=None, client_secret=None, scope=None):

        if scope is None:
            scope = "R"

        if client_id is None:
            client_id = "f2a1ed52710d4533bde25be6da03b6e3"

        if client_secret is None:
            client_secret = "ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q"

        data = {'client_id': client_id, 'client_secret': client_secret, 'scope': scope}
        return self.get_auth_token(data)

    def fetch_car_details(self):
        return self.retrieve_car_details(auth_token=self.fetch_token(scope="R").json().get("auth_token"))

    def get_count_of_all_cars(self):
        response = self.retrieve_car_details(self.fetch_token(scope="R").json().get("auth_token"))
        list_of_cars = response.json().get("data")
        return len(list_of_cars)
