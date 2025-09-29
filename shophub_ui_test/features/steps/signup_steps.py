import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.signup_page import SignupPage
from shophub_ui_test.pages.success_page import SuccessPage
from shophub_ui_test.pages.base_page import BasePage
from shophub_ui_test.utils.helpers import generate_registration_info
from selenium.common.exceptions import TimeoutException


load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

@given('el usuario ingresa a la página de registro')
def step_impl(context):
    print("context.driver:", getattr(context, "driver", None))
    context.base_page = BasePage(context.driver)
    context.signup_page = SignupPage(context.driver)
    context.success_page = SuccessPage(context.driver)
    context.signup_page.load()
    # context.base_page.assert_current_url_is_correct(context.login_page.URL)

@when('el usuario introduce información de registro válidas')
def step_impl(context):
    signup_data = generate_registration_info()
    context.signup_page.signup(signup_data["first_name"],
                             signup_data["last_name"],
                             signup_data["email"],
                             signup_data["password"],
                             signup_data["zip_code"])

@then('debería ver la página "/signup/success" el texto de "Signup Successful"')
def step_impl(context):
    context.success_page.success_message_h1("Signup Successful")

@when('el usuario registrado hace clic en el botón "Go to Home"')
def step_impl(context):
    context.success_page.go_to_home_page()