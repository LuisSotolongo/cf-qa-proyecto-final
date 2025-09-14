import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.home_page import HomePage
from shophub_ui_test.pages.success_page import SuccessPage
from shophub_ui_test.pages.base_page import BasePage
from shophub_ui_test.utils.helpers import generate_login_info
from selenium.common.exceptions import TimeoutException

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")


@given('el usuario ingresa a la página de inicio')
def step_impl(context):
    print("context.driver:", getattr(context, "driver", None))
    context.base_page = BasePage(context.driver)
    context.home_page = HomePage(context.driver)
    # context.success_page = SuccessPage(context.driver)
    context.home_page.load()
    # context.base_page.assert_current_url_is_correct(context.login_page.URL)

@when('el usuario hace clic en el logo del sitio')
def step_impl(context):
    context.home_page.go_to_home_page_logo()

@then('el usuario permanece en la página de inicio')
def step_impl(context):
    try:
        context.base_page.current_url_is_correct(SHOPHUB_BASE_URL)
    except TimeoutException:
        current_url = context.driver.current_url
        raise AssertionError(f"URL actual '{current_url}' no coincide con la URL esperada '{SHOPHUB_BASE_URL}'")


@when('el usuario hace clic en el menú desplegable "Categories"')
def step_impl(context):
    context.home_page.click_categories_dropdown()

@then('debería ver las opciones "Electronics", "Clothes" y "Books"')
def step_impl(context):
    expected_options = ["Electronics", "Clothes", "Books"]
    actual_options = context.home_page.get_categories_options()
    for option in expected_options:
        assert option in actual_options, f"Opción esperada '{option}' no encontrada en el menú desplegable 'Categories'"

@then('el usuario debería ser redirigido a la página de "Electronics"')
def step_impl(context):
    assert "electronics" in context.driver.current_url.lower()

@then('la página debería mostrar productos de "Electronics"')
def step_impl(context):
    productos = context.home_page.get_product_titles()
    assert any("electronic" in p.lower() for p in productos)

@when('el usuario hace clic en el botón de "Login"')
def step_impl(context):
    context.home_page.click_login()

@then('el usuario debería ser redirigido a la página de "Login"')
def step_impl(context):
    url_esperada = f"{SHOPHUB_BASE_URL}login"
    context.base_page.current_url_is_correct(url_esperada)


@when('el usuario hace clic en el botón de "Sign Up"')
def step_impl(context):
    context.home_page.click_signup()

@then('el usuario debería ser redirigido a la página de "Sign Up"')
def step_impl(context):
    url_esperada = f"{SHOPHUB_BASE_URL}signup"
    context.base_page.current_url_is_correct(url_esperada)

@when('el usuario hace clic en la imagen de la categoría "Men\'s Clothes"')
def step_impl(context):
    context.home_page.click_category_image()

@then('el usuario debería ser redirigido a la página de "Men\'s Clothes"')
def step_impl(context):
    url_esperada = f"{SHOPHUB_BASE_URL}categories/men-clothes"
    context.base_page.current_url_is_correct(url_esperada)

@when('el usuario hace clic en el botón "View All Deals"')
def step_impl(context):
    context.home_page.click_view_all_deals()

@then('el usuario debería ser redirigido a la página de "Special Deals"')
def step_impl(context):
    url_esperada = f"{SHOPHUB_BASE_URL}categories/special-deals"
    context.base_page.current_url_is_correct(url_esperada)