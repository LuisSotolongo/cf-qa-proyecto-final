import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.cart_page import CartPage
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

@given('el usuario ingresa a la página de inicio "HomePage"')
def step_impl(context):
    context.base_page = BasePage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.cart_page.load()

@when('el usuario selecciona un producto y hace clic en "Añadir al carrito"')
def step_add_product(context):
    context.cart_page.add_product_to_cart()

@then('el producto debería aparecer en el carrito')
def step_product_in_cart(context):
    assert context.cart_page.is_product_in_cart("Laptop")

@given('el usuario tiene productos en el carrito "eliminar producto"')
def step_given_products_for_remove(context):
    pass

@when('el usuario elimina un producto del carrito')
def step_remove_product(context):
    context.cart_page.remove_product_from_cart()

@then('el producto ya no debería aparecer en el carrito')
def step_product_not_in_cart(context):
    assert not context.cart_page.is_product_in_cart("Laptop")

@given('el usuario tiene productos en el carrito')
def step_given_products(context):
    pass

@when('el usuario actualiza la cantidad de un producto')
def step_update_quantity(context):
    context.cart_page.update_product_quantity(2)

@then('la cantidad del producto en el carrito debería reflejar el cambio')
def step_quantity_reflected(context):
    cantidad = context.cart_page.get_product_quantity("Smartphone")
    assert cantidad == 2, f"Se esperaban 2 unidades, pero hay {cantidad}"

@when('el usuario hace clic en "Proceder al pago"')
def step_checkout(context):
    context.cart_page.proceed_to_checkout()

@then('debería ser redirigido a la página de checkout')
def step_redirect_checkout(context):
    url_esperada = f"{os.getenv('SHOPHUB_BASE_URL')}checkout"
    context.base_page.current_url_is_correct(url_esperada)
