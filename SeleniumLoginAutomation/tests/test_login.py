import pytest
from SeleniumLoginAutomation.pages.login_page import LoginPage


def test_login(driver):
    driver.get('https://www.saucedemo.com/')
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()
    # Add assertions here to verify successful login
    assert "Swag Labs" in driver.title
