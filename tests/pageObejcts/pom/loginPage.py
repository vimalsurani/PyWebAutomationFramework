from selenium.webdriver.common.by import By

from tests.utils.commom_utils import webdriver_wait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_address_textbox = (By.ID, "login-username")
    password_textbox = (By.ID, "login-password")
    sign_in_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    def get_email_address(self):
        return self.driver.find_element(*LoginPage.email_address_textbox)

    def get_password_address(self):
        return self.driver.find_element(*LoginPage.password_textbox)

    def get_sign_in_button(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.email_address_textbox, timeout=5)
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self, email, pwd):
        self.get_email_address().send_keys(email)
        self.get_password_address().send_keys(pwd)
        self.get_sign_in_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text


