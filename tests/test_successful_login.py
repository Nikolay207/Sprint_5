from urls import Urls
from locators  import TestLocators
import data

class TestSuccessfulLogin:
    def test_successful_login(driver):
        driver.get(Urls.HOME_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_BUTTON).send_keys(data.VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
        assert driver.find_element(*TestLocators.LOGIN).text == 'User.','Имя пользователя отсутствует'
        element = driver.find_element(*TestLocators.AVATAR)
        assert element.is_displayed(), 'аватар пользователя отсутствует'