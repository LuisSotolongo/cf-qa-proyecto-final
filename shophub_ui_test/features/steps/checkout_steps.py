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
    pass

@then('debería ver un resumen de los productos y el total a pagar')
def step_impl(context):
    pass


# @then('debería ver la página de confirmación de compra')
# def step_should_see_confirmation_page(context):
#     # Verificar que se muestra la página de confirmación
#     pass
#
# @then('debería ver un mensaje indicando que el carrito está vacío')
# def step_should_see_empty_cart_message(context):
#     # Verificar que se muestra el mensaje de carrito vacío
#     pass
