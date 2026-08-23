import pytest
from automation_framework.config.config import Config
from automation_framework.pages.login_page import LoginPage
from automation_framework.pages.inventory_page import InventoryPage
from automation_framework.pages.cart_page import CartPage
from automation_framework.pages.checkout_page import CheckoutPage

class TestCheckoutE2E:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_complete_guest_checkout_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.VALID_USER, Config.PASSWORD)

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        assert inventory_page.get_cart_badge_count() == "2"
        inventory_page.navigate_to_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_total_cart_items_count() == 2
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_information("Alex", "Turner", "94105")
        checkout_page.complete_order()
        
        confirmation_msg = checkout_page.get_order_confirmation_text()
        assert confirmation_msg == "Thank you for your order!"