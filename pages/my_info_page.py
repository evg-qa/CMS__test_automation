import allure

from base.base_page import BasePage
from config.urls import Urls
from locators.my_info_page_locators import MyInfoPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class MyInfoPage(BasePage):

    PAGE_URL = Urls.MY_INFO_PAGE

    def change_first_name(self, new_first_name):
        with allure.step(f"Change First Name on {new_first_name}"):
            self.name = new_first_name
            first_name_field = self.wait.until(EC.element_to_be_clickable(MyInfoPageLocators.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "А")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_first_name)

    @allure.step("Click 'Save' button")
    def click_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(MyInfoPageLocators.FIRST_SAVE_BTN)).click()

    @allure.step("Check saved changes")
    def check_saved_changes(self):
        self.wait.until(EC.invisibility_of_element_located(MyInfoPageLocators.SPINNER))
        self.wait.until(EC.text_to_be_present_in_element_value(MyInfoPageLocators.FIRST_NAME_FIELD, self.name))
        self.wait.until(EC.visibility_of_element_located(MyInfoPageLocators.FIRST_NAME_FIELD))
        self.wait.until(EC.invisibility_of_element_located(MyInfoPageLocators.SUCCESSFULLY_UPDATED_MESSAGE))


