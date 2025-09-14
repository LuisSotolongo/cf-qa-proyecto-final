import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")


class CartPage(BasePage):
    URL = SHOPHUB_BASE_URL


    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.XPATH, "//a[@href='/cart']")
        self.electronics_image = (By.XPATH, "//h3[text()=\"Electronics\"]/ancestor::a")
        self.add_to_cart_laptop = (By.ID, "add-to-cart-22")
        self.add_to_cart_smartphone = (By.ID, "add-to-cart-21")
        self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
        self.h3_text_laptop = (By.XPATH, "//h3[text()='Laptop']")
        self.laptop_remove_button = (By.XPATH, "//h3[text()='Laptop']/ancestor::div[contains(@class,'flex')]/following-sibling::div//button[contains(text(),'Remove')]")
        self.plus_button_smartphone = (By.XPATH, "//h3[text()='Smartphone']/following::button[2]")
        self.proceed_to_checkout_button = (By.XPATH, "//a[@href='/checkout']/button[contains(text(),'Proceed to Checkout')]")


    def load(self):
        self.driver.get(self.URL)


    def add_product_to_cart(self):
        self.click(self.electronics_image)
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.add_to_cart_laptop)
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.add_to_cart_smartphone)


    def is_product_in_cart(self, product_name):
        self.click(self.cart_icon)
        self.wait_for_invisibility_of_element(self.loader)
        try:
            locator = (By.XPATH, f"//h3[text()='{product_name}']")
            return self.text_of_element(locator) == product_name
        except NoSuchElementException:
            return False


    def open_cart(self):
        self.click(self.cart_icon)
        self.wait_for_invisibility_of_element(self.loader)


    def remove_product_from_cart(self):
        self.open_cart()
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.laptop_remove_button)


    def update_product_quantity(self, quantity):
        self.open_cart()
        self.wait_for_invisibility_of_element(self.loader)
        for _ in range(quantity - 1):
            self.click(self.plus_button_smartphone)


    def get_product_quantity(self, product_name):
        cantidad_xpath = f"//h3[text()='{product_name}']/ancestor::div[contains(@class,'flex')]//span[contains(@class,'text-center')]"
        cantidad_element = self.driver.find_element_by_xpath(cantidad_xpath)
        return int(cantidad_element.text)


    def proceed_to_checkout(self):
        self.open_cart()
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.proceed_to_checkout_button)
        self.wait_for_invisibility_of_element(self.loader)
