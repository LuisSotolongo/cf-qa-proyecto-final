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

**Objetivo:** Validar el login y la obtención de tokens de acceso.

- **Prueba happy path:** Login con credenciales válidas  
  _Test:_ [`test_login_valid.py`](tests/auth/test_login_valid.py)  
  _Salida esperada:_ token generado, código 200  
  _Requisito:_ TA-01 Login exitoso

- **Prueba negativa:** Login con credenciales incorrectas  
  _Test:_ [`test_login_invalid.py`](tests/auth/test_login_invalid.py)  
  _Salida esperada:_ error, código 401  
  _Requisito:_ TA-02 Validación de credenciales

**Trazabilidad:** Estas pruebas validan el acceso seguro y la generación de tokens.

---

### Usuarios (`/users`)

**Objetivo:** Comprobar registro, login y consulta de usuarios.

- **Prueba happy path:** Registro con datos válidos  
  _Test:_ [`test_register_user_valido.py`](tests/users/test_register_user_valido.py)  
  _Salida esperada:_ usuario creado, código 201  
  _Requisito:_ TA-03 Registro único de usuario

- **Prueba negativa:** Registro con email ya usado  
  _Test:_ [`test_register_email_repetido.py`](tests/users/test_register_email_repetido.py)  
  _Salida esperada:_ error, código 409  
  _Requisito:_ TA-04 Validación de email único

**Trazabilidad:** Validan el registro único y autenticación segura.

---

### Aeropuertos (`/airports`)

**Objetivo:** Validar consulta, alta, edición y eliminación de aeropuertos.

- **Prueba happy path:** Consultar todos los aeropuertos  
  _Test:_ [`test_get_all_airports.py`](tests/airports/test_get_all_airports.py)  
  _Salida esperada:_ lista de aeropuertos, código 200  
  _Requisito:_ TA-05 Consulta de aeropuertos

- **Prueba happy path:** Crear aeropuerto nuevo  
  _Test:_ [`test_create_airport.py`](tests/airports/test_create_airport.py)  
  _Salida esperada:_ aeropuerto creado, código 201  
  _Requisito:_ TA-06 Alta de aeropuerto

- **Prueba happy path:** Modificar aeropuerto existente  
  _Test:_ [`test_update_airport.py`](tests/airports/test_update_airport.py)  
  _Salida esperada:_ datos actualizados, código 200  
  _Requisito:_ TA-07 Edición de aeropuerto

- **Prueba happy path:** Borrar aeropuerto  
  _Test:_ [`test_delete_airport.py`](tests/airports/test_delete_airport.py)  
  _Salida esperada:_ aeropuerto eliminado, código 204  
  _Requisito:_ TA-08 Eliminación de aeropuerto

- **Prueba negativa:** Consultar aeropuerto inexistente  
  _Test:_ [`test_get_airport_not_found.py`](tests/airports/test_get_airport_not_found.py)  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-09 Manejo de errores en consulta

- **Prueba negativa:** Crear aeropuerto con datos incompletos  
  _Test:_ [`test_create_airport_incomplete.py`](tests/airports/test_create_airport_incomplete.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-10 Validación de datos obligatorios

**Trazabilidad:** Cada prueba está vinculada al requisito funcional de gestión de aeropuertos.

---

### Vuelos (`/flights`)

**Objetivo:** Validar consulta, alta, edición y cancelación de vuelos.

- **Prueba happy path:** Consultar todos los vuelos  
  _Test:_ [`test_get_all_flights.py`](tests/flights/test_get_all_flights.py)  
  _Salida esperada:_ lista de vuelos, código 200  
  _Requisito:_ TA-11 Consulta de vuelos

- **Prueba happy path:** Crear vuelo nuevo  
  _Test:_ [`test_create_flight.py`](tests/flights/test_create_flight.py)  
  _Salida esperada:_ vuelo creado, código 201  
  _Requisito:_ TA-12 Alta de vuelo

- **Prueba happy path:** Modificar vuelo existente  
  _Test:_ [`test_update_flight.py`](tests/flights/test_update_flight.py)  
  _Salida esperada:_ datos actualizados, código 200  
  _Requisito:_ TA-13 Edición de vuelo

- **Prueba happy path:** Cancelar vuelo  
  _Test:_ [`test_cancel_flight.py`](tests/flights/test_cancel_flight.py)  
  _Salida esperada:_ vuelo cancelado, código 204  
  _Requisito:_ TA-14 Cancelación de vuelo

- **Prueba negativa:** Consultar vuelo inexistente  
  _Test:_ [`test_get_flight_not_found.py`](tests/flights/test_get_flight_not_found.py)  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-15 Manejo de errores en consulta

- **Prueba negativa:** Crear vuelo con datos incompletos  
  _Test:_ [`test_create_flight_incomplete.py`](tests/flights/test_create_flight_incomplete.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-16 Validación de datos obligatorios

**Trazabilidad:** Cada prueba está vinculada al requisito funcional de gestión de vuelos.

---

### Reservas (`/bookings`)

**Objetivo:** Validar alta, consulta, edición y cancelación de reservas.

- **Prueba happy path:** Crear reserva  
  _Test:_ [`test_create_booking.py`](tests/bookings/test_create_booking.py)  
  _Salida esperada:_ reserva creada, código 201  
  _Requisito:_ TA-17 Alta de reserva

- **Prueba happy path:** Consultar reservas  
  _Test:_ [`test_get_all_bookings.py`](tests/bookings/test_get_all_bookings.py)  
  _Salida esperada:_ lista de reservas, código 200  
  _Requisito:_ TA-18 Consulta de reservas

- **Prueba happy path:** Modificar reserva  
  _Test:_ [`test_update_booking.py`](tests/bookings/test_update_booking.py)  
  _Salida esperada:_ datos actualizados, código 200  
  _Requisito:_ TA-19 Edición de reserva

- **Prueba happy path:** Cancelar reserva  
  _Test:_ [`test_cancel_booking.py`](tests/bookings/test_cancel_booking.py)  
  _Salida esperada:_ reserva cancelada, código 204  
  _Requisito:_ TA-20 Cancelación de reserva

- **Prueba negativa:** Consultar reserva inexistente  
  _Test:_ [`test_get_booking_not_found.py`](tests/bookings/test_get_booking_not_found.py)  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-21 Manejo de errores en consulta

- **Prueba negativa:** Crear reserva con datos incompletos  
  _Test:_ [`test_create_booking_incomplete.py`](tests/bookings/test_create_booking_incomplete.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-22 Validación de datos obligatorios

**Trazabilidad:** Cada prueba está vinculada al requisito funcional de gestión de reservas.

---

### Pagos (`/payments`)

**Objetivo:** Validar el procesamiento y la validación de pagos.

- **Prueba happy path:** Pago con tarjeta válida  
  _Test:_ [`test_payment_valid_card.py`](tests/payments/test_payment_valid_card.py)  
  _Salida esperada:_ pago aceptado, código 201  
  _Requisito:_ TA-23 Procesamiento de pago exitoso

- **Prueba negativa:** Pago con tarjeta vencida  
  _Test:_ [`test_payment_expired_card.py`](tests/payments/test_payment_expired_card.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-24 Validación de fecha de vencimiento

- **Prueba negativa:** Pago con datos incompletos  
  _Test:_ [`test_payment_incomplete_data.py`](tests/payments/test_payment_incomplete_data.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-25 Validación de datos obligatorios

- **Prueba negativa:** Pago con monto inválido  
  _Test:_ [`test_payment_invalid_amount.py`](tests/payments/test_payment_invalid_amount.py)  
  _Salida esperada:_ error, código 422  
  _Requisito:_ TA-26 Validación de monto

**Trazabilidad:** Cada prueba está vinculada al requisito funcional de procesamiento y validación de pagos.

---

### Aeronaves (`/aircraft`)

**Objetivo:** Validar consulta, alta, edición y baja de aeronaves.

- **Prueba happy path:** Consultar todas las aeronaves  
  _Test:_ [`test_get_all_aircraft.py`](tests/aircraft/test_get_all_aircraft.py)  
  _Salida esperada:_ lista de aeronaves, código 200  
  _Requisito:_ TA-27 Consulta de aeronaves

- **Prueba happy path:** Crear aeronave nueva  
  _Test:_ [`test_create_aircraft.py`](tests/aircraft/test_create_aircraft.py)  
  _Salida esperada:_ aeronave creada, código 201  
  _Requisito:_ TA-28 Alta de aeronave

- **Prueba happy path:** Modificar aeronave existente  
  _Test:_ [`test_update_aircraft.py`](tests/aircraft/test_update_aircraft.py)  
  _Salida esperada:_ datos actualizados, código 200  
  _Requisito:_ TA-29 Edición de aeronave

- **Prueba happy path:** Borrar aeronave  
  _Test:_ [`test_delete_aircraft.py`](tests/aircraft/test_delete_aircraft.py)  
  _Salida esperada:_ aeronave eliminada, código 204  
  _Requisito:_ TA-30 Eliminación de aeronave

- **Prueba negativa:** Consultar aeronave inexistente  
  _Test:_ [`test_get_aircraft_not_found.py`](tests/aircraft/test_get_aircraft_not_found.py)  
  _Salida esperada:_ error, código 404  
  _Requisito:_ TA-31 Manejo de errores en consulta

- **Prueba negativa:** Crear aeronave con datos incompletos  
  _Test:_ [`test_create_aircraft_incomplete.py`](tests/aircraft/test_create_aircraft_incomplete.py)  
  _Salida esperada:_ error, código 400  
  _Requisito:_ TA-32 Validación de datos obligatorios

**Trazabilidad:** Cada prueba está vinculada al requisito funcional de gestión de aeronaves.

---

## ¿Qué faltaría para mejorar?

- Revisar que todos los casos límite estén cubiertos (campos vacíos, datos máximos).
- Añadir más pruebas negativas (errores de autenticación, formatos incorrectos).
- Documentar cada test con su requisito asociado.

---

## Reporte de pruebas

[Ver reporte Allure](reports/allure_html/index.html)
[Ver reporte Pytest-HTML](reports/html_reports/report.html)
[Ver reporte Pytest-HTML especificos pruebas](reports/html_reports/glitch_xxxxxx.html)

---

### Reintentos en tests inestables

Para mejorar la confiabilidad de la suite, uso el decorador `@pytest.mark.retry` en los tests que presentan fallos intermitentes. Ejemplo:

Esto reintentará el test hasta 2 veces, con 5 segundos de espera entre intentos.

@pytest.mark.retry(retries=2, delay=5)
def test_inestable():
    # código del test

---