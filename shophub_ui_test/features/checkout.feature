Feature: Checkout del carrito

  Background:
    Given el usario tiene productos en el carrito checkout

  Scenario: Proceder al checkout con productos en el carrito
    When el usuario procede al checkout
    Then debería ver la página de confirmación de compra


  Scenario: Validar información de envío en el checkout
    When el usuario procede al checkout e ingresa la información de envío
    Then la información de envío debería guardarse correctamente
    Then debería ver la página de confirmación de compra envio


  Scenario: Mostrar mensaje de alerta si faltan campos obligatorios en el checkout
  When el usuario intenta proceder al checkout sin completar los campos obligatorios
  Then debería ver un mensaje de alerta indicando "Please fill in all required fields"