import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.login_page import LoginPage
from shophub_ui_test.pages.success_page import SuccessPage
from shophub_ui_test.pages.base_page import BasePage
from shophub_ui_test.utils.helpers import generate_login_info
from selenium.common.exceptions import TimeoutException


load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

@given('el usuario ingresa a la página de login')
def step_impl(context):
    context.base_page = BasePage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.success_page = SuccessPage(context.driver)
    context.login_page.load()

@when('el usuario introduce credenciales válidas')
def step_impl(context):
    login_data = generate_login_info()
    context.login_page.login(login_data["email"], login_data["password"])

@then('debería ver la página "login/success" el texto de "Logged In"')
def step_impl(context):
    context.success_page.success_message_h1("Logged In")

@when('el usuario hace clic en el botón "Go to Home"')
def step_impl(context):
    context.success_page.go_to_home_page()


@when('el usuario introduce un email sin arroba y una contraseña válida')
def step_impl(context):
    login_data = generate_login_info()
    email_without_at = re.sub('@', '', login_data["email"])
    context.login_page.login(email_without_at, login_data["password"])

@when('el usuario deja el campo email vacío y introduce una contraseña válida')
def step_impl(context):
    login_data = generate_login_info()
    context.login_page.login("", login_data["password"])

@when('el usuario introduce un email válido y deja la contraseña vacía')
def step_impl(context):
    login_data = generate_login_info()
    context.login_page.login(login_data["email"], "")


@then('no me deberia permitir iniciar sesión, debo continuar en la página de login')
def step_impl(context):
    context.login_page.assert_login_page_not_left, "No se quedó en la página de login"

