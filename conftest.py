import pytest
from selenium import webdriver
import random
from data import letters

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def random_email():
    return f"user{random.randint(100, 999)}@mail.ru"

@pytest.fixture(scope='function')
def invalid_email():
    return (random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) +
    '@' + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters))