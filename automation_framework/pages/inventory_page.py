from selenium.webdriver.common.by import By
from automation_framework.pages.base_page import BasePage

class InventoryPage(BasePage):
    PRODUCT_BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    PRODUCT_BIKE_LIGHT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click(self.PRODUCT_BACKPACK_ADD_BTN)

    def add_bike_light_to_cart(self):
        self.click(self.PRODUCT_BIKE_LIGHT_ADD_BTN)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def navigate_to_cart(self):
        self.click(self.CART_LINK)