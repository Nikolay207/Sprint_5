from urls import Urls
from locators  import TestLocators


def test_create_listing_unauthorized(driver):
    driver.get(Urls.HOME_URL)
    driver.find_element(*TestLocators.CREATE_LISTING).click()
    assert driver.find_element(*TestLocators.CREATE_LISTING_TITLE).is_displayed()