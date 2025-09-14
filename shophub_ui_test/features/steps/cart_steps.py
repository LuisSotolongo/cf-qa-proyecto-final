import os
import re
from behave import given, when, then
from dotenv import load_dotenv
from shophub_ui_test.pages.cart_page import CartPage
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

@given('el usuario ingresa a la página de inicio "cart"')
def step_impl(context):
    print("context.driver:", getattr(context, "driver", None))
    context.base_page = BasePage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.cart_page.load()

@when('el usuario selecciona un producto y hace clic en "Añadir al carrito"')
def step_add_product(context):
    context.cart_page.add_product_to_cart()

@then('el producto debería aparecer en el carrito')
def step_product_in_cart(context):
    assert context.cart_page.is_product_in_cart("Laptop")

@given('el usuario tiene productos en el carrito "ver productos"')
def step_given_products_in_cart(context):
    context.cart_page.add_product_to_cart("Producto Ejemplo")

@when('el usuario accede al carrito')
def step_open_cart(context):
    context.cart_page.open_cart()

@then('debería ver la lista de productos añadidos')
def step_see_products(context):
    products = context.cart_page.get_cart_products()
    assert "Producto Ejemplo" in products

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
    context.cart_page.update_product_quantity()

@then('la cantidad del producto en el carrito debería reflejar el cambio')
def step_quantity_reflected(context):
    pass

@given('el usuario tiene productos en el carrito "vaciar carrito"')
def step_given_products_for_empty(context):
    pass

@when('el usuario vacía el carrito')
def step_empty_cart(context):
    context.cart_page.empty_cart()

@then('el carrito debería estar vacío')
def step_cart_empty(context):
    assert context.cart_page.is_cart_empty()

@when('el usuario hace clic en "Proceder al pago"')
def step_checkout(context):
    context.cart_page.proceed_to_checkout()

@then('debería ser redirigido a la página de checkout')
def step_redirect_checkout(context):
    url_esperada = f"{os.getenv('SHOPHUB_BASE_URL')}checkout"
    context.base_page.current_url_is_correct(url_esperada)
