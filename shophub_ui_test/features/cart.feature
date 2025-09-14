Feature: Funcionalidades del carrito de compra
  Como usuario de la tienda
  Quiero añadir, ver y eliminar productos en mi carrito
  Para gestionar mi compra antes de pagar

  Background:
    Given el usuario ingresa a la página de inicio "cart"

  Scenario: Añadir un producto al carrito
    When el usuario selecciona un producto y hace clic en "Añadir al carrito"
    Then el producto debería aparecer en el carrito


  Scenario: Eliminar un producto del carrito
    Given el usuario tiene productos en el carrito "eliminar producto"
    When el usuario elimina un producto del carrito
    Then el producto ya no debería aparecer en el carrito

  Scenario: Actualizar la cantidad de un producto en el carrito
    Given el usuario tiene productos en el carrito
    When el usuario actualiza la cantidad de un producto
    Then la cantidad del producto en el carrito debería reflejar el cambio

  Scenario: Vaciar el carrito
    Given el usuario tiene productos en el carrito "vaciar carrito"
    When el usuario vacía el carrito
    Then el carrito debería estar vacío

  Scenario: Proceder al checkout desde el carrito
    Given el usuario tiene productos en el carrito
    When el usuario hace clic en "Proceder al pago"
    Then debería ser redirigido a la página de checkout
