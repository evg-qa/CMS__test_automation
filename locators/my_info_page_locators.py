from selenium.webdriver.common.by import By

class MyInfoPageLocators:

    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    FIRST_SAVE_BTN = (By.XPATH, "(//button[@type='submit'])[1]")
    SPINNER = (By.XPATH, "//div[@class='oxd-loading-spinner']")
    SUCCESSFULLY_UPDATED_MESSAGE = (By.XPATH, "//p[text()='Successfully Updated']")
