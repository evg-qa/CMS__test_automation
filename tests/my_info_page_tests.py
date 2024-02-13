import random
from base.base_test import BaseTest

class TestMyInfoPage(BaseTest):

    def test_change_first_name(self):
        self.login_page.open()
        self.login_page.input_login(self.data.LOGIN)
        self.login_page.input_password(self.data.PASSWORD)
        self.login_page.click_submit_btn()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_btn()
        self.my_info_page.change_first_name(f"Name {random.randint(1, 10)}")
        self.my_info_page.click_save_btn()
        self.my_info_page.check_save_changes()


