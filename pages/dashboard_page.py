import allure
from base.base_page import BasePage
from configuration.urls import Urls
from locators.dashboard_page_locators import DashboardPageLocators
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = Urls.DASHBOARD_PAGE

    @allure.step("Click 'My info' button")
    def click_my_info_btn(self):
        self.wait.until(EC.element_to_be_clickable(DashboardPageLocators.MY_INFO_BTN)).click()
