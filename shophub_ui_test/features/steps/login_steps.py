import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.login_page import LoginPage
from shophub_ui_test.pages.login_success_page import LoginSuccessPage
from shophub_ui_test.pages.base_page import BasePage
from shophub_ui_test.utils.helpers import generate_login_info
from selenium.common.exceptions import TimeoutException


load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

@given('el usuario ingresa a la página de login')
def step_impl(context):
    print("context.driver:", getattr(context, "driver", None))
    context.base_page = BasePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.login_success_page = LoginSuccessPage(context.driver)
    context.login_page.load()
    # context.base_page.assert_current_url_is_correct(context.login_page.URL)

@when('el usuario introduce credenciales válidas')
def step_impl(context):
    login_data = generate_login_info()
    context.login_page.login(login_data["email"], login_data["password"])

@then('debería ver la página el texto de "Logged In"')
def step_impl(context):
    context.login_success_page.login_success_message_h1("Logged In")

@when('el usuario hace clic en el botón "Go to Home"')
def step_impl(context):
    context.login_success_page.go_to_home_page()


# @when('el usuario introduce un email sin arroba y una contraseña válida')
# def step_impl(context):
#     login_data = generate_login_info()
#     email_without_at = re.sub('@', '', login_data["email"])
#     context.login_page.login(email_without_at, login_data["password"])
#
# @when('el usuario deja el campo email vacío y introduce una contraseña válida')
# def step_impl(context):
#     login_data = generate_login_info()
#     context.login_page.login("", login_data["password"])
#
# @when('el usuario introduce un email válido y deja la contraseña vacía')
# def step_impl(context):
#     login_data = generate_login_info()
#     context.login_page.login(login_data["email"], "")
#
# @then('debería ver la página segura "/login/success"')
# def step_impl(context):
#     context.base_page.assert_current_url_is_correct(f"{context.login_page.URL}/success")
#
# @then('debería ver un mensaje de error')
# def step_impl(context):
#     try:
#         context.login_page.assert_error_message_is_visible()
#     except TimeoutException:
#         raise AssertionError("El mensaje de error no apareció en la página.")
