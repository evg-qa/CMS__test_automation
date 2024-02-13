from base.base_test import BaseTest

class TestDashboardPageFeature(BaseTest):

    def test_click_my_info_btn(self):
        self.dashboard_page.click_my_info_btn()
