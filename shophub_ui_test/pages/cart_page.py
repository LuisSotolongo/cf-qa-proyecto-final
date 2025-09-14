import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shophub_ui_test.pages.base_page import BasePage

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

class CartPage(BasePage):

      def __init__(self, driver):
          self.driver = driver
          self.cart_icon = (By.XPATH, "//a[@href='/cart']")
          self.electronics_image = (By.XPATH, "//h3[text()=\"Men's Clothes\"]/ancestor::a")
          self.add_to_cart_laptop = (By.ID, "add-to-cart-22")
          self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
          self.h3_text_laptop = (By.XPATH, "//h3[text()='Laptop']")
          self.remove_button = (By.XPATH, "//button[contains(text(),'Remove')]")



    def add_product_to_cart(self):
        self.click(self.electronics_image)
        self.wait_for_invisibility_of_element(self.loader)


    def is_product_in_cart(self, product_name):
        self.click(self.cart_icon)
        self.wait_for_invisibility_of_element(self.loader)
        self.text_of_element(self.h3_text_laptop)
        return self.text_of_element(self.h3_text_laptop) == product_name

    def open_cart(self):
        self.click(self.cart_icon)
        self.wait_for_invisibility_of_element(self.loader)

    def get_cart_products(self):
        self.open_cart()


    def remove_product_from_cart(self, product_name):
        self.open_cart()



    def update_product_quantity(self, product_name, quantity):
        self.open_cart()


    def get_product_quantity(self, product_name):
        self.open_cart()


    def empty_cart(self):
        self.open_cart()


    def is_cart_empty(self):
        self.open_cart()


    def proceed_to_checkout(self):
        self.open_cart()

