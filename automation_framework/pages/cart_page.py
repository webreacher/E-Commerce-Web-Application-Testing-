from selenium.webdriver.common.by import By
from automation_framework.pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def get_total_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))