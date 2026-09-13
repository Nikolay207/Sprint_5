from urls import Urls
from locators  import TestLocators
import data

from helpers import generate_invalid_email

email = generate_invalid_email()

class TestInvalidEmailError:
    def test_invalid_email_error(self,driver):
        driver.get(Urls.HOME_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_BUTTON).send_keys(email)
        driver.find_element(*TestLocators.INPUT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
        driver.find_element(*TestLocators.REPEAT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
        driver.find_element(*TestLocators.CREATE_ACCOUNT).click()
        error_text = driver.find_element(*TestLocators.INVALID_EMAIL_ERROR)
        email_error = driver.find_element(*TestLocators.EMAIL_ERROR)
        password_error = driver.find_element(*TestLocators.PASSWORD_ERROR)
        repeat_error = driver.find_element(*TestLocators.REPEAT_PASSWORD_ERROR)
        assert error_text.is_displayed(), "текст ошибки не выводится"
        assert email_error.is_displayed(), "нет красной обводки у поля Email"
        assert password_error.is_displayed(), "нет красной обводки у поля Пароль"
        assert repeat_error.is_displayed(), "нет красной обводки у поля Повторите пароль"
