from faker import Faker

fake = Faker('es_ES')


def generate_unique_email():
    return fake.unique.email()


def generate_registration_info():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": generate_unique_email(),
        "password": fake.password(length=10),
        "zip_code": fake.postcode()
    }

def generate_login_info():
    return {
        "email": generate_unique_email(),
        "password": fake.password(length=10)
    }


def generate_payment_info():
    return {
        "card_number": fake.credit_card_number(),
        "expiration_date": fake.credit_card_expire(),
        "cvv": fake.credit_card_security_code()
    }



def generate_post_order():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": generate_unique_email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "city": "Las Palmas De Gran Canaria",
        "zip_code": "33355",
        "country": "Spain",
    }