from tests.utils.commom_utils import webdriver_wait_url
from seleniumpagefactory.Pagefactory import PageFactory


class DashboardPage(PageFactory):  # TODO - 1. Single Inheritance
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'username_logged_in': ('XPATH', "//span[@data-qa='lufexuloga']")
    }

    def user_logged_in_text(self):
        webdriver_wait_url(driver=self.driver, timeout=20)
        return self.username_logged_in.get_text()
