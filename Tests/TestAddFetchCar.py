from Utils.ErrorMsg import ErrorMsg
from Utils.Api import APITestWrapper
from Utils.StatusCode import StatusCode


class TestAddFetchCar():
    def setup(self):
        self.api_wrapper = APITestWrapper()
        self.error_msgs = ErrorMsg()
        self.prepare_data()

    def prepare_data(self):
        self.incorrect_auth_token = "Y2U0ODk3ZDZlMTQwZjgxZmQ2Mjg0NWFlMTEwN2EzMDA5YTM5NjQ0YjNkNTRiZmExZDY4MWY0YjMyN2M2YjBmYg=="
        self.correct_value_for_model = "model"
        self.correct_value_for_brand = "brand"
        self.correct_value_for_power_rating = 1
        self.correct_value_for_daily_price = 1
        self.brand_or_model_name_not_a_string = 1
        self.brand_or_model_name_empty_string = ""
        self.brand_or_model_name_max_length_string = "whatisthelongestbrandnamethathisfieldcanactuallytakeissomethngthaIamtestingherebecauseIdonthaveanyspecificationforthat"
        self.brand_or_model_name_with_special_characters = "Th|s!s@$peci@lCh@recterM0delN@m*"
        self.value_greater_than_zero = 1
        self.value_less_than_zero = 0
        self.value_equal_to_zero = 0
        self.value_greater_than_500 = 501
        self.value_equal_to_500 = 500
        self.value_less_than_500 = 499
        self.value_not_an_integer = "thisIsNotAnInteger"

    def assert_error_msg(self, actual_response, expected_error_msg, expected_error_code):
        actual_error_code = actual_response.status_code
        actual_errormsg = actual_response.json().get("errorMessage")
        assert expected_error_code == actual_error_code, "Verify Status code"
        assert expected_error_msg == actual_errormsg, "Verify Error message"

    def assert_count_of_car(self, expected_count):
        assert expected_count == self.api_wrapper.get_count_of_all_cars()

    def test_add_a_car_with_brand_name_correct_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car()
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_brand_name_not_a_string(self):
        r = self.api_wrapper.add_new_car(brand=self.brand_or_model_name_not_a_string)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_type_int("brand", key_value="1"), StatusCode.HTTP_400)

    def test_add_a_car_with_brand_name_empty_string(self):
        r = self.api_wrapper.add_new_car(brand=self.brand_or_model_name_empty_string)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_type_unicode("brand", key_value=""),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_brand_name_max_length_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(brand=self.brand_or_model_name_max_length_string)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_brand_name_with_special_characters_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(brand=self.brand_or_model_name_with_special_characters)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_model_name_correct_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(model=self.correct_value_for_model)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_model_name_not_a_string(self):
        r = self.api_wrapper.add_new_car(model=self.brand_or_model_name_not_a_string)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_type_int("model", key_value="1"), StatusCode.HTTP_400)

    def test_add_a_car_with_model_name_empty_string(self):
        r = self.api_wrapper.add_new_car(model=self.brand_or_model_name_empty_string)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_type_unicode("model", key_value=""),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_model_name_max_length_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(model=self.brand_or_model_name_max_length_string)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_model_name_with_special_characters_string(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(model=self.brand_or_model_name_with_special_characters)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_power_rating_greater_than_zero(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(power_rating=self.value_greater_than_zero)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_power_rating_less_than_zero(self):
        r = self.api_wrapper.add_new_car(power_rating=self.value_less_than_zero)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_range('power_rating', key_value=self.value_less_than_zero),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_power_rating_equal_to_zero(self):
        r = self.api_wrapper.add_new_car(power_rating=self.value_equal_to_zero)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_range('power_rating', key_value=self.value_equal_to_zero),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_power_rating_greater_than_500(self):
        r = self.api_wrapper.add_new_car(power_rating=self.value_greater_than_500)
        self.assert_error_msg(r,
                              self.error_msgs.msg_invalid_range('power_rating', key_value=self.value_greater_than_500),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_power_rating_less_than_500(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(power_rating=self.value_less_than_500)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_power_rating_equal_to_500(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(power_rating=self.value_equal_to_500)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_power_rating_not_an_integer(self):
        r = self.api_wrapper.add_new_car(power_rating=self.value_not_an_integer)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_type_unicode('power_rating',
                                                                          key_value=self.value_not_an_integer),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_daily_price_greater_than_zero(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(daily_price=self.value_greater_than_zero)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_daily_price_less_than_zero(self):
        r = self.api_wrapper.add_new_car(daily_price=self.value_less_than_zero)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_range('daily_price', key_value=self.value_less_than_zero),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_daily_price_equal_to_zero(self):
        r = self.api_wrapper.add_new_car(daily_price=self.value_equal_to_zero)
        self.assert_error_msg(r, self.error_msgs.msg_invalid_range('daily_price', key_value=self.value_equal_to_zero),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_daily_price_greater_than_500(self):
        r = self.api_wrapper.add_new_car(daily_price=self.value_greater_than_500)
        self.assert_error_msg(r,
                              self.error_msgs.msg_invalid_range('daily_price', key_value=self.value_greater_than_500),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_daily_price_less_than_500(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(daily_price=self.value_less_than_500)
        self.assert_count_of_car(current_count + 1)

    def test_add_a_car_with_daily_price_value_equal_to_500(self):
        current_count = self.api_wrapper.get_count_of_all_cars()
        r = self.api_wrapper.add_new_car(daily_price=self.value_equal_to_500)
        self.assert_count_of_car(current_count + 1)

    #
    def test_add_a_car_with_daily_price_value_not_an_integer(self):
        r = self.api_wrapper.add_new_car(daily_price=self.value_not_an_integer)
        self.assert_error_msg(r,
                              self.error_msgs.msg_invalid_type_unicode('daily_price', key_value=self.value_not_an_integer),
                              StatusCode.HTTP_400)

    def test_add_a_car_with_incorrect_token(self):
        r = self.api_wrapper.add_new_car(auth_token=self.incorrect_auth_token)
        self.assert_error_msg(r, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)
