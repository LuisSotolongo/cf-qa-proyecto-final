Feature: Autenticacion de usuario - Login

  Como usuario registrado
  Quiero poder iniciar sesión
  Para acceder a mis funcionalidades restringidas

  Background:
    Given el usuario ingresa a la página de login

  Scenario: Login exitoso
    When el usuario introduce credenciales válidas
    Then debería ver la página "login/success" el texto de "Logged In"
    When el usuario hace clic en el botón "Go to Home"


 Scenario: Login fallido por email sin arroba
  When el usuario introduce un email sin arroba y una contraseña válida
  Then no me deberia permitir iniciar sesión, debo continuar en la página de login

Scenario: Login fallido por email vacío
  When el usuario deja el campo email vacío y introduce una contraseña válida
  Then no me deberia permitir iniciar sesión, debo continuar en la página de login

Scenario: Login fallido por contraseña vacía
  When el usuario introduce un email válido y deja la contraseña vacía
  Then no me deberia permitir iniciar sesión, debo continuar en la página de login