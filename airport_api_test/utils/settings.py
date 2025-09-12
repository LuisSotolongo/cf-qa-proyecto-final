# Endpoints de autenticación (Auth)
# POST
AUTH_SIGNUP = "/auth/signup"  # Registro de usuario
AUTH_LOGIN = "/auth/login"    # Inicio de sesión

# Endpoints de usuarios (Users)
# POST
USERS = "/users"                      # Crear usuario como admin
# GET
USERS_LIST = "/users"                 # Listar usuarios
USERS_ME = "/users/me"                # Obtener usuario actual
# PUT
USER_UPDATE = "/users/{user_id}"      # Actualizar usuario
# DELETE
USER_DELETE = "/users/{user_id}"      # Eliminar usuario


# Endpoints de aeropuertos (Airports)
# POST
AIRPORTS = "/airports"                        # Crear aeropuerto
# GET
AIRPORTS_LIST = "/airports"                   # Listar aeropuertos
AIRPORT_DETAIL_GET = "/airports/{iata_code}"  # Obtener aeropuerto
# PUT
AIRPORT_UPDATE = "/airports/{iata_code}"      # Actualizar aeropuerto
# DELETE
AIRPORT_DELETE = "/airports/{iata_code}"      # Eliminar aeropuerto



# Endpoints de vuelos (Flights)
# POST
FLIGHTS = "/flights"                        # Crear vuelo
# GET
FLIGHTS_LIST = "/flights"                   # Buscar vuelos
FLIGHT_DETAIL_GET = "/flights/{flight_id}"  # Obtener vuelo
# PUT
FLIGHT_UPDATE = "/flights/{flight_id}"      # Actualizar vuelo
# DELETE
FLIGHT_DELETE = "/flights/{flight_id}"      # Eliminar vuelo



# Endpoints de reservas (Bookings)
# POST
BOOKINGS = "/bookings"                          # Crear reserva
# GET
BOOKINGS_LIST = "/bookings"                     # Listar reservas
BOOKING_DETAIL_GET = "/bookings/{booking_id}"   # Obtener reserva
# PATCH
BOOKING_PATCH = "/bookings/{booking_id}"        # Actualizar reserva
# DELETE
BOOKING_DELETE = "/bookings/{booking_id}"       # Cancelar reserva



# Endpoints de pagos (Payments)
# POST
PAYMENTS = "/payments"                          # Realizar pago
# GET
PAYMENT_DETAIL_GET = "/payments/{payment_id}"   # Obtener pago



# Endpoints de aeronaves (Aircrafts)
# POST
AIRCRAFTS = "/aircrafts"                          # Crear aeronave
# GET
AIRCRAFTS_LIST = "/aircrafts"                     # Listar aeronaves
AIRCRAFT_DETAIL_GET = "/aircrafts/{aircraft_id}"  # Obtener aeronave
# PUT
AIRCRAFT_UPDATE = "/aircrafts/{aircraft_id}"      # Actualizar aeronave
# DELETE
AIRCRAFT_DELETE = "/aircrafts/{aircraft_id}"      # Eliminar aeronave



# Endpoints de ejemplos de error (Glitch Examples)
# GET
GLITCH_SUCCESS_BUT_ERROR = "/glitch-examples/success-but-error"  # Success But Error
GLITCH_CLIENT_ERROR = "/glitch-examples/client-error"            # Client Error
GLITCH_SERVER_ERROR = "/glitch-examples/server-error"            # Server Error
GLITCH_TIMEOUT = "/glitch-examples/timeout"                      # Timeout Error
