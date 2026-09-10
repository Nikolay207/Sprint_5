from urls import Urls
from locators  import TestLocators
import data

def test_successful_registration(driver,random_email):
    driver.get(Urls.HOME_URL)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.NO_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.INPUT_EMAIL_BUTTON).send_keys(random_email)
    driver.find_element(*TestLocators.INPUT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
    driver.find_element(*TestLocators.REPEAT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
    driver.find_element(*TestLocators.CREATE_ACCOUNT).click()
    assert driver.find_element(*TestLocators.LOGIN).text == 'User.','Имя пользователя отсутствует'
    element = driver.find_element(*TestLocators.AVATAR)
    assert element.is_displayed(), 'аватар пользователя отсутствует'
