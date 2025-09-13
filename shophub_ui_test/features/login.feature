Feature: Autenticacion de usuario - Login

  Como usuario registrado
  Quiero poder iniciar sesión
  Para acceder a mis funcionalidades restringidas

  Scenario: Login exitoso
    Given el usuario ingresa a la página de login
    When el usuario introduce credenciales válidas
    Then debería ver la página el texto de "Logged In"
    When el usuario hace clic en el botón "Go to Home"


# Scenario: Login fallido por email sin arroba
#  Given el usuario ingresa a la página de login
#  When el usuario introduce un email sin arroba y una contraseña válida
#  Then debería ver un mensaje de error
#
#Scenario: Login fallido por email vacío
#  Given el usuario ingresa a la página de login
#  When el usuario deja el campo email vacío y introduce una contraseña válida
#  Then debería ver un mensaje de error
#
#Scenario: Login fallido por contraseña vacía
#  Given el usuario ingresa a la página de login
#  When el usuario introduce un email válido y deja la contraseña vacía
#  Then debería ver un mensaje de error