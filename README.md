# cf-qa-proyecto-final
Proyecto final del Bootcamp QA Testing Automatizado
===================================================================================
---

## Instalación del entorno y dependencias

Si clonas mi proyecto desde GitHub con `git clone`, lo primero es crear el entorno virtual en Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Luego instala las dependencias necesarias de Python:

```bash
pip install -r requirements.txt
```

**Nota:** Para generar el archivo `requirements.txt` después de instalar las dependencias, puedes usar:

```bash
pip3 freeze > requirements.txt
```

## Herramientas principales utilizadas

- behave
- selenium
- pytest-
- requests
- webdriver-manager

---

## Pruebas para la API

## Endpoints cubiertos en las pruebas

**Auth**

- POST `/auth/signup` - Signup
- POST `/auth/login` - Login

**Users**

- POST `/users` - Create User As Admin
- GET `/users` - List Users
- GET `/users/me` - Me
- PUT `/users/{user_id}` - Update User
- DELETE `/users/{user_id}` - Delete User

**Airports**

- POST `/airports` - Create Airport
- GET `/airports` - List Airports
- GET `/airports/{iata_code}` - Get Airport
- PUT `/airports/{iata_code}` - Update Airport
- DELETE `/airports/{iata_code}` - Delete Airport

**Flights**

- POST `/flights` - Create Flight
- GET `/flights` - Search Flights
- GET `/flights/{flight_id}` - Get Flight
- PUT `/flights/{flight_id}` - Update Flight
- DELETE `/flights/{flight_id}` - Delete Flight

**Bookings**

- POST `/bookings` - Create Booking
- GET `/bookings` - List Bookings
- GET `/bookings/{booking_id}` - Get Booking
- PATCH `/bookings/{booking_id}` - Update Booking
- DELETE `/bookings/{booking_id}` - Cancel Booking


**Aircrafts**

- POST `/aircrafts` - Create Aircraft
- GET `/aircrafts` - List Aircrafts
- GET `/aircrafts/{aircraft_id}` - Get Aircraft
- PUT `/aircrafts/{aircraft_id}` - Update Aircraft
- DELETE `/aircrafts/{aircraft_id}` - Delete Aircraft


---

Las pruebas se realizan sobre estos endpoints utilizando las herramientas mencionadas.
