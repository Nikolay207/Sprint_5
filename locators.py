from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_BUTTON = By.XPATH, "//div/button[text()='Вход и регистрация']"
    NO_ACCOUNT_BUTTON = By.XPATH, "//div/button[text()='Нет аккаунта']"
    INPUT_EMAIL_BUTTON = By.XPATH, "//div/input[@placeholder = 'Введите Email']"
    INPUT_PASSWORD_BUTTON = By.XPATH, "//div/input[@placeholder = 'Пароль']"
    REPEAT_PASSWORD_BUTTON = By.XPATH, "//div/input[@placeholder = 'Повторите пароль']"
    CREATE_ACCOUNT = By.XPATH, "//div/button[text()='Создать аккаунт']"
    LOGIN = By.XPATH, "//h3[text()='User.']"
    AVATAR = By.XPATH, "//button[@class = 'circleSmall']"
    INVALID_EMAIL_ERROR = By.XPATH, "//div/span[text() = 'Ошибка']"
    EMAIL_ERROR = (By.XPATH, "(//div[@class='input_inputError__fLUP9'])[1]")
    PASSWORD_ERROR = (By.XPATH, "(//div[@class='input_inputError__fLUP9'])[2]")
    REPEAT_PASSWORD_ERROR = (By.XPATH, "(//div[@class='input_inputError__fLUP9'])[3]")
    LOGIN_SUBMIT_BUTTON = By.XPATH, "//div/button[text()='Войти']"
    LOGOUT_BUTTON = By.XPATH, "//div/button[text()='Выйти']"
    CREATE_LISTING = By.XPATH, "//div/button[text()='Разместить объявление']"
    CREATE_LISTING_TITLE = By.XPATH, "//form/div/h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    NAME_INPUT = By.XPATH, "//div/input[@placeholder = 'Название']"
    DESCRIPTION_INPUT = By.XPATH, "//div/textarea[@placeholder = 'Описание товара']"
    PRICE_INPUT = By.XPATH, "//div/input[@placeholder = 'Стоимость']"
    CATEGORY_SELECT_BUTTON = (By.XPATH, "//input[@name='category']/ancestor::div[contains(@class, 'dropDownMenu_input')]//button")
    CATEGORY_SUBMIT_BUTTON = By.XPATH, "//div/button/span[text()='Книги']"
    CITY_SELECT_BUTTON = (By.XPATH, "//input[@name='city']/ancestor::div[contains(@class, 'dropDownMenu_input')]//button")
    CITY_SUBMIT_BUTTON = By.XPATH, "//div/button/span[text()='Санкт-Петербург']"
    PUBLISH_BUTTON = By.XPATH, "//form/button[text()='Опубликовать']"
    LISTING_CARDS = (By.CSS_SELECTOR, "div.card")