from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def visit(self, url: str):
        self.driver.get(url)

    def click(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def type(self, locator: tuple[By, str], text: str):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def text_of_element(self, locator: tuple[By, str]) -> str:
        return self.driver.find_element(*locator).text

    def element_is_visible(self, locator: tuple[By, str]) -> bool:
        return self.driver.find_element(*locator).is_displayed()

    def reload(self):
        self.driver.refresh()

    def wait_until_visible(self, locator: tuple[By, str], timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def wait_for_element(self, locator: tuple[By, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility_of_element(self, locator: tuple[By, str], timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def current_url_is_correct(self, url_esperada, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == url_esperada)
        except TimeoutException:
            current_url = self.driver.current_url
            raise AssertionError(f"URL actual '{current_url}' no coincide con la URL esperada '{url_esperada}'")