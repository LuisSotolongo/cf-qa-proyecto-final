import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shophub_ui_test.pages.base_page import BasePage


SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

class LoginSuccessPage(BasePage):

    URL = f"{SHOPHUB_BASE_URL}/login/success"

    def __init__(self, driver):
        self.driver = driver
        self.h1_logged_in = (By.XPATH, "//h1[text()='Logged In']")
        self.go_home_button = (By.XPATH, "//button[text()='Go to Home']")
        self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")

    def login_success_message_h1(self, expected_text_h1):
        try:
            welcome_message = self.wait_for_element(self.h1_logged_in)
            assert welcome_message.text == expected_text_h1, (
                f"Texto del <h1> incorrecto. Esperado: '{expected_text_h1}', "
                f"Obtenido: '{welcome_message.text}'"
            )
        except TimeoutException:
            raise AssertionError("El mensaje de bienvenida <h1> no se encontró en la página.")

    def go_to_home_page(self):
        self.wait_for_invisibility_of_element(self.loader)
        self.click(self.go_home_button)