import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.cart_page import CartPage
from shophub_ui_test.pages.checkout_page import CheckoutPage
from shophub_ui_test.pages.success_page import SuccessPage
from shophub_ui_test.utils.helpers import generate_post_order
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

@given('el usario tiene productos en el carrito checkout')
def step_impl(context):
    context.base_page = BasePage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)
    context.cart_page.load()
    context.cart_page.add_product_to_cart()

@when('el usuario procede al checkout')
def step_impl(context):
    context.checkout_page.open_checkout_page()


@then('debería ver la página de confirmación de compra')
def step_impl(context):
    context.checkout_page.checkout_is_not_empty()



@when('el usuario procede al checkout e ingresa la información de envío')
def step_impl(context):
    context.checkout_page.open_checkout_page()
    fill_form_post_order = generate_post_order()
    context.checkout_page.fill_checkout_form(
        fill_form_post_order["first_name"],
        fill_form_post_order["last_name"],
        fill_form_post_order["email"],
        fill_form_post_order["phone"],
        fill_form_post_order["address"],
        fill_form_post_order["city"],
        fill_form_post_order["zip_code"],
        fill_form_post_order["country"]
    )


@then('la información de envío debería guardarse correctamente')
def step_impl(context):
    assert context.checkout_page.is_shipping_info_displayed(), "La información de envío no se guardó correctamente"


@then('debería ver la página de confirmación de compra envio')
def step_should_see_confirmation_page(context):
    assert context.driver.current_url.endswith("/confirmation"), "No está en la página de confirmación"
    texto = context.checkout_page.get_confirmation_header_text()
    if "No Order Found" in texto:
        screenshot_path = "shophub_ui_test/reports/failed_screenshots/confirmation_page_bug.png"
        context.driver.save_screenshot(screenshot_path)
        print(f"BUG: Mensaje incorrecto en la página de confirmación. Captura guardada en: {screenshot_path}")
        raise AssertionError("BUG: Se muestra 'No Order Found' en vez del mensaje de confirmación")


@when('el usuario intenta proceder al checkout sin completar los campos obligatorios')
def step_impl(context):
    context.checkout_page.open_checkout_page()
    context.checkout_page.click_place_order_button()

@then('debería ver un mensaje de alerta indicando "Please fill in all required fields"')
def step_impl(context):
    context.checkout_page.handle_alert("Please fill in all required fields")