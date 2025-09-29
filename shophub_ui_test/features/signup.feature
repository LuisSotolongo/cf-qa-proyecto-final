Feature: Registro de usuario - Sign-in

  Como nuevo usuario
  Quiero poder registrarme
  Para poder acceder a las funcionalidades de la plataforma

  Scenario: Registro de usuario exitoso
    Given el usuario ingresa a la página de registro
    When el usuario introduce información de registro válidas
    Then debería ver la página "/signup/success" el texto de "Signup Successful"
    When el usuario registrado hace clic en el botón "Go to Home"
