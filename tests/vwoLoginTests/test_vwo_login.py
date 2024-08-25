import time

import allure
import pytest
from selenium import webdriver

from tests.pageObejcts.pom.dashboardPage import DashboardPage
from tests.pageObejcts.pom.loginPage import LoginPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(email="vimalpatel7449@gmail.com", pwd="Abc@12456")
    time.sleep(2)
    error_msg_element = login_page.get_error_message_text()
    assert error_msg_element == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#2 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(email="vimalpatel7449@gmail.com", pwd="Abc@123456")
    dashboardPage = DashboardPage(driver=setup)
    assert "Vimal Patel" in dashboardPage.user_logged_in_text()
