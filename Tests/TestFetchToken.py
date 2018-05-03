from Utils.ErrorMsg import ErrorMsg
from Utils.StatusCode import StatusCode
from Utils.Api import APITestWrapper


class TestFetchToken:
    def setup(self):
        self.api_wrapper = APITestWrapper()
        self.error_msgs = ErrorMsg()
        self.prepare_test_data()

    def prepare_test_data(self):
        self.missing_client_id_for_write = self.api_wrapper.fetch_token(client_id='', scope='W').json().get("auth_token")
        self.incorrect_client_id_for_write = self.api_wrapper.fetch_token(client_id='#$$%%^&*((*&^%$#@%^&',
                                                                          scope='W').json().get("auth_token")

        self.missing_client_id_for_read = self.api_wrapper.fetch_token(client_id='', scope='R').json().get("auth_token")
        self.incorrect_client_id_for_read = self.api_wrapper.fetch_token(client_id='#$$%%^&*((*&^%$#@%^&',
                                                                         scope='R').json().get("auth_token")

        self.missing_client_secret_for_write = self.api_wrapper.fetch_token(client_secret='', scope='W').json().get("auth_token")
        self.invalid_client_secret_for_write = self.api_wrapper.fetch_token(
            client_secret='#$$%%^&*((*&^%$#@@#$%^&', scope='W').json().get("auth_token")

        self.missing_client_secret_for_read = self.api_wrapper.fetch_token(client_secret='', scope='R').json().get("auth_token")
        self.invalid_client_secret_for_read = self.api_wrapper.fetch_token(
            client_secret='#$$%%^&*((*&^%$#@@#$%^&', scope='R').json().get("auth_token")

        self.missing_scope_for_auth_token = self.api_wrapper.fetch_token(scope='').json().get("auth_token")
        self.invalid_scope_for_auth_token = self.api_wrapper.fetch_token(scope='@@').json().get("auth_token")

    def assert_error_msg(self, actual_response, expected_error_msg, expected_error_code):
        actual_error_code = actual_response.status_code
        actual_errormsg = actual_response.json().get("errorMessage")
        assert expected_error_code == actual_error_code, "Verify Status code"
        assert expected_error_msg == actual_errormsg, "Verify Error message"

    def test_auth_token_with_correct_parameters_for_token_write(self):
        response = self.api_wrapper.fetch_token(scope='R')
        assert response.status_code == StatusCode.HTTP_200

    def test_auth_token_with_missing_client_id_for_token_write(self):
        r = self.api_wrapper.fetch_token(client_id=self.missing_client_id_for_write)
        self.assert_error_msg(r,
                              self.error_msgs.msg_missing_wrong_input_data(), StatusCode.HTTP_400)

    def test_auth_token_incorrect_client_id_for_token_write(self):
        invalid_token = self.api_wrapper.fetch_token(client_id=self.incorrect_client_id_for_write).json().get(
            "auth_token")
        r2 = self.api_wrapper.add_new_car(auth_token=invalid_token)
        self.assert_error_msg(r2, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)

    def test_auth_token_with_missing_client_secret_for_token_write(self):
        r = self.api_wrapper.fetch_token(client_secret=self.missing_client_secret_for_write)
        self.assert_error_msg(r,
                              self.error_msgs.msg_missing_wrong_input_data(), StatusCode.HTTP_400)

    def test_auth_token_incorrect_client_secret_for_token_write(self):
        invalid_token = self.api_wrapper.fetch_token(client_secret=self.invalid_client_secret_for_write).json().get(
            "auth_token")
        r2 = self.api_wrapper.add_new_car(auth_token=invalid_token)
        self.assert_error_msg(r2, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)

    def test_auth_token_with_missing_client_id_for_token_read(self):
        r = self.api_wrapper.fetch_token(client_id=self.missing_client_id_for_read)
        self.assert_error_msg(r,
                              self.error_msgs.msg_missing_wrong_input_data(), StatusCode.HTTP_400)

    def test_auth_token_incorrect_client_id_for_token_read(self):
        invalid_token = self.api_wrapper.fetch_token(client_id=self.incorrect_client_id_for_read).json().get(
            "auth_token")
        r2 = self.api_wrapper.add_new_car(auth_token=invalid_token)
        self.assert_error_msg(r2, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)

    def test_auth_token_with_missing_client_secret_for_token_read(self):
        r = self.api_wrapper.fetch_token(client_secret=self.missing_client_secret_for_read)
        self.assert_error_msg(r,
                              self.error_msgs.msg_missing_wrong_input_data(), StatusCode.HTTP_400)

    def test_auth_token_incorrect_client_secret_for_token_read(self):
        invalid_token = self.api_wrapper.fetch_token(client_secret=self.invalid_client_secret_for_read).json().get(
            "auth_token")
        r2 = self.api_wrapper.add_new_car(auth_token=invalid_token)
        self.assert_error_msg(r2, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)

    def test_auth_token_with_missing_scope_for_token(self):
        r = self.api_wrapper.fetch_token(scope=self.missing_scope_for_auth_token)
        self.assert_error_msg(r,
                              self.error_msgs.msg_missing_wrong_input_data(), StatusCode.HTTP_400)

    def test_auth_token_incorrect_scope_for_token(self):
        invalid_token = self.api_wrapper.fetch_token(scope=self.invalid_scope_for_auth_token).json().get("auth_token")
        r2 = self.api_wrapper.add_new_car(auth_token=invalid_token)
        self.assert_error_msg(r2, self.error_msgs.errormsg_invalid_permission(), StatusCode.HTTP_401)
