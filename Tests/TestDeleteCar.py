import json

from Utils.ErrorMsg import ErrorMsg
from Utils.Api import APITestWrapper


class TestDeleteCar:
    def setup(self):
        self.api_wrapper = APITestWrapper()
        self.read_auth_token = self.api_wrapper.fetch_token(scope='R').json().get("auth_token")
        self.write_auth_token = self.api_wrapper.fetch_token(scope='W').json().get("auth_token")
        self.error_msgs = ErrorMsg()
        self.prepare_test_data()

    def prepare_test_data(self):
        self.model_name_of_car_to_delete = "maruti"
        self.non_existing_car_id = 10000000000
        self.correct_model_name = "model"

    def delete_car_based_on_id(self, car_id):
        response = self.api_wrapper.delete_car(car_id, self.write_auth_token).json().get("success")
        if response == True:
            return True
        else:
            return False

    def fetch_car_id_from_unique_model(self, model):
        data = self.api_wrapper.fetch_car_details().json().get("data")

        data_for_model = {}
        count = 0
        for d in data:
            if d.get("model") == model:
                data_for_model[count] = d
                count = count + 1

        if (count) == 1:
            return data_for_model[0].get("car_id")
        elif (count) == 0:
            return "No cars for this model"
        else:
            return "More than one car for the given model " + model

    def delete_cars_for_given_model(self, model):
        data = self.api_wrapper.fetch_car_details().json().get("data")
        found_flag = False
        for d in data:
            if d.get("model") == model:
                found_flag = True
                if self.delete_car_based_on_id(int(d.get("car_id"))):
                    found_flag = True
        return found_flag

    def test_delete_all_existing_cars(self):
        response = self.api_wrapper.retrieve_car_details(self.write_auth_token)
        data = json.loads(response.text)
        ids = [element['car_id'] for element in data['data']]
        for car_id in ids:
            assert self.delete_car_based_on_id(car_id), "Deletion successful"

    def test_add_and_delete_a_car_for_given_model_with_write_token(self):
        self.api_wrapper.add_new_car()
        assert self.delete_cars_for_given_model(self.correct_model_name), "Delete car for a given model is successful"

    def test_add_and_delete_a_car_with_read_token(self):
        self.api_wrapper.add_new_car()
        response = self.api_wrapper.delete_car("21389123", self.read_auth_token)
        assert response.status_code == 401, "Status code check as 401"

    def test_delete_a_car_for_given_model_name(self):
        self.api_wrapper.add_new_car(model=self.model_name_of_car_to_delete)
        res = self.fetch_car_id_from_unique_model(self.model_name_of_car_to_delete)
        if type(res) == int:
            assert self.delete_car_based_on_id(res), "Deletion successful"
        else:
            assert False, res

    def test_try_delete_a_car_for_given_model_with_multiple_entries(self):
        self.api_wrapper.add_new_car(model=self.model_name_of_car_to_delete)
        self.api_wrapper.add_new_car(model=self.model_name_of_car_to_delete)
        res = self.fetch_car_id_from_unique_model(self.model_name_of_car_to_delete)
        if type(res) == int:
            assert False, "False positive : Deletion successful for car with multiple entries"
        else:
            assert True, res

    def test_try_delete_a_car_for_given_model_with_no_entries(self):
        res = self.fetch_car_id_from_unique_model("ljsajdsaljdiasd")
        if type(res) == int:
            assert False, "False positive: Deletion succesful for a non existing car"
        else:
            assert True, res + ": Expected behaviour for a non existing car deletion"

    def test_delete_a_non_existing_car_id(self):
        response = self.api_wrapper.retrieve_car_details(self.write_auth_token)
        data = json.loads(response.text)
        ids = [element['car_id'] for element in data['data']]
        if self.non_existing_car_id in ids:
            assert False, "This car_id exists"
        else:
            r = self.delete_car_based_on_id(self.non_existing_car_id)
        assert r == False
