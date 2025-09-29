Guía de Prerrequisitos y Escenarios de Prueba para SHOPHUB
===========================================================================
Esta guía describe los prerrequisitos y escenarios cubiertos por las pruebas automatizadas del sitio de e-commerce SHOPHUB, organizados en flujos positivos y negativos, conforme a los archivos feature implementados.

Pruebas de Flujo Positivo (Happy Path)
---------------------------------------
Las pruebas de flujo positivo validan el comportamiento esperado ante acciones correctas del usuario, asegurando que las funcionalidades principales operan correctamente.

Escenarios cubiertos:

1. Registro y Autenticación
   - Registro exitoso de usuario (signup.feature)
   - Login exitoso con credenciales válidas (login.feature)

2. Navegación y Usabilidad
   - Acceso y navegación en la página principal, incluyendo interacción con el header, navegación a login, registro, categorías y ofertas especiales (home.feature)

3. Gestión del Carrito
   - Añadir productos al carrito (cart.feature)
   - Eliminar productos del carrito (cart.feature)
   - Actualizar la cantidad de productos en el carrito (cart.feature)
   - Proceder al checkout desde el carrito (cart.feature)

4. Proceso de Checkout
   - Proceder al checkout con productos en el carrito (checkout.feature)
   - Ingreso y validación de información de envío (checkout.feature)

Pruebas de Flujo Negativo
-------------------------
Las pruebas de flujo negativo verifican la robustez del sistema ante entradas inválidas o acciones incorrectas, asegurando que se gestionan adecuadamente los errores y restricciones.

Escenarios cubiertos:

1. Checkout
   - Intentar proceder al checkout sin completar los campos obligatorios, mostrando mensaje de alerta: "Please fill in all required fields" (checkout.feature)

2. Login fallidos
   - Intento de login con email sin arroba
   - Intento de login con email vacío
   - Intento de login con contraseña vacía

Importancia de la Cobertura
---------------------------
La combinación de pruebas positivas y negativas permite validar tanto el funcionamiento esperado como la capacidad de la plataforma para manejar errores y restricciones, garantizando una experiencia de usuario robusta y segura.

Para ampliar la cobertura negativa, se recomienda activar y mantener los escenarios de login negativo, así como agregar casos adicionales en otras funcionalidades críticas.

Guía rápida para ejecutar pruebas con Behave
-------------------------------------------
Behave es la herramienta utilizada para la ejecución de pruebas BDD (Behavior Driven Development) en este proyecto. Asegúrate de ejecutar los comandos desde la carpeta shophub_ui_test, donde se encuentran los directorios features y steps.

Para ejecutar todas las pruebas:

    behave

Para ejecutar únicamente las pruebas de login (archivo específico):

    behave features/login.feature

Ejecución de escenarios específicos
----------------------------------
Puedes ejecutar escenarios concretos utilizando etiquetas o el nombre del escenario:

- Por nombre de escenario (por ejemplo, "Login exitoso"):

    behave -n "Login exitoso"

Notas importantes
-----------------
- La opción -n espera el nombre exacto de un escenario, no un archivo.

