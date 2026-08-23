import pytest
from automation_framework.config.config import Config
from automation_framework.pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.VALID_USER, Config.PASSWORD)
        
        assert "inventory.html" in login_page.get_current_url()

    @pytest.mark.negative
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.LOCKED_USER, Config.PASSWORD)
        
        error_text = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_text

    @pytest.mark.negative
    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.VALID_USER, "wrong_password_123")
        
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text