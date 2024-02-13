import allure
from base.base_test import BaseTest


class TestLoginPage(BaseTest):

    @allure.step("Authorization with valid data")
    @allure.severity("Critical")
    def test_authorization(self):
        self.login_page.open()
        self.login_page.input_login(self.data.LOGIN)
        self.login_page.input_password(self.data.PASSWORD)
        self.login_page.click_submit_btn()
        self.dashboard_page.is_opened()


