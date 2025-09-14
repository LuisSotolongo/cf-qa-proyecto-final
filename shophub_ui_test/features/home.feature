Feature: Funcionalidades del Home Page

  Como usuario de la tienda
  Quiero interactuar con la página de inicio
  Para navegar por la tienda y descubrir productos

  Background:
    Given el usuario ingresa a la página de inicio

  Scenario: Interacción con los elementos del encabezado (header)
    When el usuario hace clic en el logo del sitio
    Then el usuario permanece en la página de inicio


  Scenario: Navegación a las páginas de Autenticación (Login y Sign Up)
    When el usuario hace clic en el botón de "Login"
    Then el usuario debería ser redirigido a la página de "Login"
    When el usuario hace clic en el botón de "Sign Up"
    Then el usuario debería ser redirigido a la página de "Sign Up"


  Scenario: Navegación a las categorías principales
    When el usuario hace clic en la imagen de la categoría "Men's Clothes"
    Then el usuario debería ser redirigido a la página de "Men's Clothes"

  Scenario: Acceso a la sección de ofertas especiales
    When el usuario hace clic en el botón "View All Deals"
    Then el usuario debería ser redirigido a la página de "Special Deals"