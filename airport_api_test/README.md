# Guía de Pruebas para la API

---

## ¿Por qué hacemos estas pruebas?

Las pruebas aseguran que la API responde correctamente tanto en casos exitosos como en situaciones de error. Así evitamos problemas en producción y garantizamos que los requisitos se cumplan.

---

## Uso de fixtures y `conftest.py`

Para propagar datos entre pruebas, usamos fixtures en `pytest`.  
Cada endpoint tiene su propio `conftest.py` para datos específicos, pero hay un `conftest.py` global con los datos de autenticación.  
El token de autenticación se usa en varios endpoints, por ejemplo en `/users`, `/airports`, `/flights`, `/bookings`, etc.  
Esto permite reutilizar el token y mantener las pruebas organizadas.

---

## Plan de pruebas y diseño de casos

---

### Autenticación (`/auth`)

- **Prueba happy path:** Login con credenciales válidas  
  _Objetivo:_ Verificar acceso con credenciales correctas  
  _Test:_ `test_login_exitoso`  
  _Salida esperada:_ token generado, código 200  
  _Requisito:_ TA-01 - Valida el acceso exitoso y la generación de token  
  _Trazabilidad:_ Garantiza el acceso seguro y la generación de tokens

- **Prueba negativa:** Login con credenciales incorrectas  
  _Objetivo:_ Validar rechazo de acceso  
  _Test:_ `test_login_fallido`  
  _Salida esperada:_ error, código 401  
  _Requisito:_ TA-02 - Valida el rechazo de credenciales inválidas  
  _Trazabilidad:_ Protección ante intentos no autorizados

- **Prueba happy path:** Registro exitoso  
  _Objetivo:_ Crear usuario y validar datos  
  _Test:_ `test_signup_exitoso`  
  _Salida esperada:_ usuario creado, código 201  
  _Requisito:_ TA-03 - Valida el registro único de usuario  
  _Trazabilidad:_ Creación segura de usuarios

- **Prueba negativa:** Registro con email existente  
  _Objetivo:_ Rechazar duplicados  
  _Test:_ `test_signup_email_existente`  
  _Salida esperada:_ error, código 400/409/422  
  _Requisito:_ TA-04 - Valida que no se permita el registro con email duplicado  
  _Trazabilidad:_ Evita duplicidad

- **Prueba negativa:** Registro con rol inválido  
  _Objetivo:_ Rechazar roles no permitidos  
  _Test:_ `test_signup_rol_invalido`  
  _Salida esperada:_ error, código 400/422/500  
  _Requisito:_ TA-05 - Valida que solo se acepten roles permitidos  
  _Trazabilidad:_ Control de roles

---

### Usuarios (`/users`)

- **Prueba happy path:** Crear usuario válido  
  _Objetivo:_ Registro único de usuario  
  _Test:_ `test_create_user_valid`  
  _Salida esperada:_ usuario creado, código 201  
  _Requisito:_ TA-03 - Valida la creación de usuarios con datos válidos  
  _Trazabilidad:_ Creación segura

- **Prueba negativa:** Crear usuario sin email  
  _Objetivo:_ Validación de email único  
  _Test:_ `test_create_user_invalid`  
  _Salida esperada:_ error, código 400/422  
  _Requisito:_ TA-04 - Valida que el email sea obligatorio y único  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Listar usuarios con paginación  
  _Objetivo:_ Listado correcto  
  _Test:_ `test_list_users`  
  _Salida esperada:_ lista, código 200  
  _Requisito:_ TA-05 - Valida la consulta paginada de usuarios  
  _Trazabilidad:_ Consulta correcta

- **Prueba happy path:** Obtener detalles del usuario autenticado  
  _Objetivo:_ Datos del usuario  
  _Test:_ `test_get_me`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-06 - Valida la obtención de datos del usuario autenticado  
  _Trazabilidad:_ Consulta de perfil

- **Prueba happy path:** Actualizar usuario válido  
  _Objetivo:_ Actualización de datos  
  _Test:_ `test_update_user_valid`  
  _Salida esperada:_ datos actualizados, código 200  
  _Requisito:_ TA-07 - Valida la actualización de datos de usuario existente  
  _Trazabilidad:_ Actualización segura

- **Prueba negativa:** Actualizar usuario inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_update_user_invalid`  
  _Salida esperada:_ error, código 404/400/422  
  _Requisito:_ TA-08 - Valida el manejo de errores al actualizar usuario no existente  
  _Trazabilidad:_ Control de errores

- **Prueba happy path:** Eliminar usuario existente  
  _Objetivo:_ Baja de usuario  
  _Test:_ `test_delete_user_valid`  
  _Salida esperada:_ eliminado, código 204  
  _Requisito:_ TA-09 - Valida la eliminación de usuario existente  
  _Trazabilidad:_ Baja segura

- **Prueba negativa:** Eliminar usuario inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_delete_user_invalid`  
  _Salida esperada:_ error, código 204/404/400/422  
  _Requisito:_ TA-10 - Valida el manejo de errores al eliminar usuario no existente  
  _Trazabilidad:_ Control de errores

---

### Aeropuertos (`/airports`)

- **Prueba happy path:** Consultar todos los aeropuertos  
  _Objetivo:_ Listado completo  
  _Test:_ `test_get_all_airports`  
  _Salida esperada:_ lista, código 200  
  _Requisito:_ TA-11 - Valida la consulta de todos los aeropuertos  
  _Trazabilidad:_ Consulta correcta

- **Prueba happy path:** Crear aeropuerto nuevo  
  _Objetivo:_ Alta de aeropuerto  
  _Test:_ `test_create_airport`  
  _Salida esperada:_ creado, código 201  
  _Requisito:_ TA-12 - Valida la creación de aeropuertos con datos válidos  
  _Trazabilidad:_ Creación segura

- **Prueba happy path:** Modificar aeropuerto  
  _Objetivo:_ Edición de datos  
  _Test:_ `test_update_airport`  
  _Salida esperada:_ actualizado, código 200  
  _Requisito:_ TA-13 - Valida la actualización de datos de aeropuerto  
  _Trazabilidad:_ Actualización

- **Prueba happy path:** Borrar aeropuerto  
  _Objetivo:_ Eliminación  
  _Test:_ `test_delete_airport`  
  _Salida esperada:_ eliminado, código 204  
  _Requisito:_ TA-14 - Valida la eliminación de aeropuerto existente  
  _Trazabilidad:_ Baja segura

- **Prueba negativa:** Consultar aeropuerto inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_get_airport_not_found`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-15 - Valida el manejo de errores al consultar aeropuerto no existente  
  _Trazabilidad:_ Control de errores

- **Prueba negativa:** Crear aeropuerto con datos incompletos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_create_airport_incomplete`  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-16 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

---

### Vuelos (`/flights`)

- **Prueba happy path:** Crear vuelo nuevo  
  _Objetivo:_ Alta de vuelo  
  _Test:_ `test_create_flight_success`  
  _Salida esperada:_ creado, código 201  
  _Requisito:_ TA-17 - Valida la creación de vuelos con datos válidos  
  _Trazabilidad:_ Creación segura

- **Prueba negativa:** Crear vuelo con datos incompletos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_create_flight_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-18 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Consultar vuelo por id  
  _Objetivo:_ Consulta de vuelo  
  _Test:_ `test_get_flight_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-19 - Valida la consulta de vuelo por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Consultar vuelo inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_get_flight_not_found`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-20 - Valida el manejo de errores al consultar vuelo no existente  
  _Trazabilidad:_ Control de errores

- **Prueba negativa:** Buscar vuelos con parámetros inválidos  
  _Objetivo:_ Validación de parámetros  
  _Test:_ `test_search_flights_invalid_params`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-21 - Valida la restricción de parámetros de búsqueda  
  _Trazabilidad:_ Validación de datos

- **Prueba de rendimiento:** Tiempo de respuesta  
  _Objetivo:_ Validar tiempo de respuesta  
  _Test:_ `test_flight_response_time`  
  _Salida esperada:_ <2 segundos, código 200  
  _Requisito:_ TA-22 - Valida el rendimiento del endpoint  
  _Trazabilidad:_ Performance

---

### Reservas (`/bookings`)

- **Prueba happy path:** Crear reserva  
  _Objetivo:_ Alta de reserva  
  _Test:_ `test_create_booking_success`  
  _Salida esperada:_ creada, código 200  
  _Requisito:_ TA-23 - Valida la creación de reservas con datos válidos  
  _Trazabilidad:_ Creación segura

- **Prueba negativa:** Crear reserva con datos incompletos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_create_booking_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-24 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Consultar todas las reservas  
  _Objetivo:_ Listado de reservas  
  _Test:_ `test_get_all_bookings_success`  
  _Salida esperada:_ lista, código 200  
  _Requisito:_ TA-25 - Valida la consulta de todas las reservas  
  _Trazabilidad:_ Consulta correcta

- **Prueba happy path:** Consultar reserva por id  
  _Objetivo:_ Consulta de reserva  
  _Test:_ `test_get_booking_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-26 - Valida la consulta de reserva por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Consultar reserva inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_get_booking_not_found`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-27 - Valida el manejo de errores al consultar reserva no existente  
  _Trazabilidad:_ Control de errores

- **Prueba happy path:** Modificar reserva  
  _Objetivo:_ Edición de datos  
  _Test:_ `test_update_booking_success`  
  _Salida esperada:_ actualizado, código 200  
  _Requisito:_ TA-28 - Valida la actualización de datos de reserva  
  _Trazabilidad:_ Actualización

- **Prueba negativa:** Modificar reserva inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_update_booking_invalid`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-29 - Valida el manejo de errores al modificar reserva no existente  
  _Trazabilidad:_ Control de errores

- **Prueba negativa:** Eliminar reserva inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_delete_booking_invalid`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-30 - Valida el manejo de errores al eliminar reserva no existente  
  _Trazabilidad:_ Control de errores

---

### Aeronaves (`/aircrafts`)

- **Prueba happy path:** Consultar aeronave por id  
  _Objetivo:_ Validar consulta por id  
  _Test:_ `test_create_aircraft_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-31 - Valida la consulta de aeronave por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Crear aeronave con datos incompletos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_create_aircraft_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-32 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Consultar aeronave por id  
  _Objetivo:_ Validar consulta por id  
  _Test:_ `test_get_aircraft_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-33 - Valida la consulta de aeronave por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Consultar aeronave inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_get_aircraft_invalid`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-34 - Valida el manejo de errores al consultar aeronave no existente  
  _Trazabilidad:_ Control de errores

- **Prueba happy path:** Modificar aeronave  
  _Objetivo:_ Edición de datos  
  _Test:_ `test_update_aircraft_success`  
  _Salida esperada:_ actualizado, código 200  
  _Requisito:_ TA-35 - Valida la actualización de datos de aeronave  
  _Trazabilidad:_ Actualización

- **Prueba negativa:** Modificar aeronave con datos incompletos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_update_aircraft_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-36 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Eliminar aeronave  
  _Objetivo:_ Baja de aeronave  
  _Test:_ `test_delete_aircraft_success`  
  _Salida esperada:_ eliminado, código 204  
  _Requisito:_ TA-37 - Valida la eliminación de aeronave existente  
  _Trazabilidad:_ Baja segura

- **Prueba negativa:** Eliminar aeronave inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_delete_aircraft_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-38 - Valida el manejo de errores al eliminar aeronave no existente  
  _Trazabilidad:_ Control de errores

---

### Pagos (`/payments`)

- **Prueba happy path:** Consultar pago por id  
  _Objetivo:_ Validar consulta por id  
  _Test:_ `test_create_payment_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-39 - Valida la consulta de pago por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Crear pago con datos inválidos  
  _Objetivo:_ Validación de datos  
  _Test:_ `test_create_payment_invalid`  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-40 - Valida que los datos obligatorios sean requeridos  
  _Trazabilidad:_ Integridad de datos

- **Prueba happy path:** Consultar pago por id  
  _Objetivo:_ Validar consulta por id  
  _Test:_ `test_get_payment_success`  
  _Salida esperada:_ datos, código 200  
  _Requisito:_ TA-41 - Valida la consulta de pago por id  
  _Trazabilidad:_ Consulta correcta

- **Prueba negativa:** Consultar pago inexistente  
  _Objetivo:_ Manejo de errores  
  _Test:_ `test_get_payment_not_found`  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-42 - Valida el manejo de errores al consultar pago no existente  
  _Trazabilidad:_ Control de errores

---


## ¿Qué faltaría para mejorar?

- Revisar que todos los casos límite estén cubiertos (campos vacíos, datos máximos).
- Añadir más pruebas negativas (errores de autenticación, formatos incorrectos).
- Documentar cada test con su requisito asociado.
- Que funcionen todos los tests a la ves, hay varios errores en payments que no he logrado resolver.

---

## Reporte de pruebas

[Ver reporte Allure](reports/allure_html/index.html)
[Ver reporte Pytest-HTML](reports/html_reports/report.html)
[Ver reporte Pytest-HTML especificos pruebas](reports/html_reports/glitch_xxxxxx.html)

---

### Reintentos en tests inestables

Para mejorar la confiabilidad de la suite, uso el decorador `@pytest.mark.retry` en los tests que presentan fallos intermitentes. Ejemplo:

Esto reintentará el test hasta 2 veces, con 5 segundos de espera entre intentos.

@pytest.mark.retry(retries=3, delay=5)
def test_inestable():
    # código del test

---