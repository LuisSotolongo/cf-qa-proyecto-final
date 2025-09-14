Feature: Checkout del carrito

  Background:
    Given el usario tiene productos en el carrito checkout

  Scenario: Proceder al checkout con productos en el carrito
    When el usuario procede al checkout
    Then debería ver la página de confirmación de compra


  Scenario: Validar información de envío en el checkout
    When el usuario procede al checkout e ingresa la información de envío
    Then la información de envío debería guardarse correctamente

  Scenario: Mostrar resumen de compra antes de confirmar
    When el usuario procede al checkout
    Then debería ver un resumen de los productos y el total a pagar

#  Scenario: No permitir checkout con el carrito vacío
#    When el usuario intenta proceder al checkout
#    Then debería ver un mensaje indicando que el carrito está vacío
