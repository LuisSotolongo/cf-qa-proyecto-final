from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def get_driver(headless=False):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(10)
    return driver