Guía de Prerrequisitos para Pruebas de SHOPHUB
===========================================================================
Esta guía describe los pasos necesarios para establecer los prerrequisitos de los escenarios de prueba del sitio de e-commerce SHOPHUB.


1. Pruebas de Flujo Positivo (Happy Path)
Las pruebas de "happy path" validan el flujo de usuario ideal, desde el inicio hasta el éxito.

Escenario: Flujo de Compra Completo
Para poder comprar un producto, el usuario debe tener un carrito lleno y una cuenta.

Prerrequisitos:

Registro de Usuario: El usuario debe haberse registrado exitosamente con información válida y haber iniciado sesión. Esto garantiza que podemos asociar una compra a una cuenta.

Búsqueda o Navegación de Producto: El usuario debe navegar a la página de un producto específico.

Adición al Carrito: El producto debe ser añadido al carrito. Esto es vital, ya que un carrito vacío no puede avanzar al checkout.

Paso a Probar: Navegar a la página de checkout y pagar.

2. Pruebas de Flujo Negativo
