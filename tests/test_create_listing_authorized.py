from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import Urls
from locators  import TestLocators
import data


def test_create_listing_authorized(driver):
    driver.get(Urls.HOME_URL)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.INPUT_EMAIL_BUTTON).send_keys(data.VALID_EMAIL)
    driver.find_element(*TestLocators.INPUT_PASSWORD_BUTTON).send_keys(data.VALID_PASSWORD)
    driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN))
    cards_before = driver.find_elements(*TestLocators.LISTING_CARDS)
    count_before = len(cards_before)
    driver.find_element(*TestLocators.CREATE_LISTING).click()
    driver.find_element(*TestLocators.NAME_INPUT).send_keys(data.VALID_NAME)
    driver.find_element(*TestLocators.DESCRIPTION_INPUT).send_keys(data.VALID_DESCRIPTION)
    driver.find_element(*TestLocators.PRICE_INPUT).send_keys(data.VALID_PRICE)
    driver.find_element(*TestLocators.CATEGORY_SELECT_BUTTON).click()
    driver.find_element(*TestLocators.CATEGORY_SUBMIT_BUTTON).click()
    driver.find_element(*TestLocators.CITY_SELECT_BUTTON).click()
    driver.find_element(*TestLocators.CITY_SUBMIT_BUTTON).click()
    driver.find_element(*TestLocators.PUBLISH_BUTTON).click()
    cards_after = driver.find_elements(*TestLocators.LISTING_CARDS)
    count_after = len(cards_after)
    assert count_after == count_before + 1, 'Количество созданных объявлений не изменилось'
