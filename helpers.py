import random
from data import letters

def generate_random_email():
    return f"user{random.randint(100, 999)}@mail.ru"

def generate_invalid_email():
    return (random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) +
            '@' + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters))