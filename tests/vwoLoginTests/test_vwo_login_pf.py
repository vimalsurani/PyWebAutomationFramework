import time
import pytest
from tests.pageObejcts.page_factory.loginPage_pf import LoginPage
from tests.pageObejcts.page_factory.dashboardPage_pf import DashboardPage
import allure
from tests.constants.constants import Constants


@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(Constants.app_url())
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="vimalpatel7449@gmail.com", pwd="123")
        error_msg_element = loginPage.error_msg()
        assert error_msg_element == "Your email, password, IP address or location did not match"

        if "Dashboard" not in driver.title:
            Constants.take_screenshot(driver, "test_vwo_login_negative_tc0")
        time.sleep(10)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user="vimalpatel7449@gmail.com", pwd="Abc@123456")
        time.sleep(20)
        dashboard_page = DashboardPage(driver)
        assert "Vimal Patel" in dashboard_page.user_logged_in_text()
        time.sleep(10)
