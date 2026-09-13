from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import Urls
from locators  import TestLocators
import data

class TestLogout:

    def test_logout(self,driver):
        driver.get(Urls.HOME_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_BUTTON).send_keys(data.VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
        assert driver.find_element(*TestLocators.LOGIN).text == 'User.', 'Имя пользователя отсутствует'
        element = driver.find_element(*TestLocators.AVATAR)
        assert element.is_displayed(), 'аватар пользователя отсутствует'
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(TestLocators.LOGIN))
        WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(TestLocators.AVATAR))
        assert driver.find_element(*TestLocators.LOGIN_BUTTON).text == 'Вход и регистрация' , 'Кнопка Вход и регистрация отсутствует'

