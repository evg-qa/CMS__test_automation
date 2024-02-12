from base.base_page import BasePage
from config.urls import Urls
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Urls.LOGIN_PAGE

    def input_login(self, login):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.USER_NAME_FIELD)).send_keys(login)

    def input_password(self, password):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(password)

    def click_submit_btn(self):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
