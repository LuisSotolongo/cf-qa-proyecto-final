import os
from dotenv import load_dotenv
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

class HomePage(BasePage):

    URL = SHOPHUB_BASE_URL or "https://shophub-demo.netlify.app/"

    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.CSS_SELECTOR, 'a.flex.items-center.space-x-2')
        self.categories_menu = (By.XPATH, "//button[text()='Categories']")
        self.men_clothes_image = (By.XPATH, "//h3[text()=\"Men's Clothes\"]/ancestor::a")
        self.special_deals_option = (By.XPATH, "//button[text()='View All Deals']/ancestor::a")
        self.search_input = (By.CSS_SELECTOR, 'input[placeholder="Search products..."]')
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.signup_button = (By.XPATH, "//button[text()='Sign Up']")
        self.cart_icon = (By.XPATH, "//a[@href='/cart']")
        self.go_home_button = (By.XPATH, "//button[text()='Go to Home']")
        self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
        self.login_message = (By.XPATH, "//div[text()='Login']")
        self.signup_message = (By.XPATH, "//div[text()='Sign Up']")


    def load(self):
        self.driver.get(self.URL)

    def go_to_home_page_logo(self):
        self.click(self.logo)

    def click_categories_dropdown(self):
        self.click(self.categories_menu)
        try:
            self.wait_for_element(self.categories_menu)
        except TimeoutException:
            raise Exception("Categories dropdown did not appear")

    def click_on_any_categoy(self):
        categories = self.driver.find_elements(By.CSS_SELECTOR, "a.dropdown-item")
        if categories:
            categories[0].click()
        else:
            raise Exception("No categories found in the dropdown")

    # def get_categories_options(self):
    #     menu = self.driver.find_element(*self.categories_menu)
    #     ActionChains(self.driver).move_to_element(menu).perform()
    #     self.wait_for_element(self.categories_options)
    #     category = self.driver.find_element(*self.categories_options)
    #     ActionChains(self.driver).move_to_element(category).click().perform()
    #     return opciones or []

    def click_login(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.login_button)

    def click_signup(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.signup_button)

    def go_to_cart_page(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.cart_icon)

    def click_category_image(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.men_clothes_image)

    def click_view_all_deals(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.special_deals_option)

    def click_go_to_home_buttomn(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.go_home_button)

    def current_url(self):
        return self.driver.current_url_is_correct