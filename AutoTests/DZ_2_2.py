import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://149.255.118.78:7080")
    yield driver
    driver.close()


# В классе AutorizationPage определяем базовые методы для работы с WebDriver
class AutorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://149.255.118.78:7080"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


# Класс SeacrhLocators для хранения локаторов
class SeacrhLocators:
    LOCATOR_SEARCH_LOGIN = (By.ID, "loginEmail")
    LOCATOR_SEARCH_PASSWORD = (By.ID, "loginPassword")
    LOCATOR_SEARCH_BUTTON = (By.ID, "authButton")
    LOCATOR_MAIN_MENU = (By.TAG_NAME, 'h3')
    LOCATOR_WRONG_EMAIL_OR_PASS = (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')
    LOCATOR_WRONG_EMAIL = (By.XPATH, '//*[contains(text(), "Неверный формат E-Mail")]')


# Вспомогательные методы для работы с поиском
class SearchHelper(AutorizationPage):
    def enter_login_pswd(self, login, pswd):
        search_field_log = self.find_element(SeacrhLocators.LOCATOR_SEARCH_LOGIN)
        search_field_log.click()
        search_field_log.send_keys(login)
        search_field_pswd = self.find_element(SeacrhLocators.LOCATOR_SEARCH_PASSWORD)
        search_field_pswd.click()
        search_field_pswd.send_keys(pswd)
        return search_field_log, search_field_pswd

    def click_on_the_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_BUTTON, time=5).click()

    def authorization_correct(self):
        return self.find_element(SeacrhLocators.LOCATOR_MAIN_MENU, time=5)

    def incorrect_email_or_pass(self):
        return self.find_element(SeacrhLocators.LOCATOR_WRONG_EMAIL_OR_PASS, time=5)

    def incorrect_email(self):
        return self.find_element(SeacrhLocators.LOCATOR_WRONG_EMAIL, time=5)


def test_1(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@protei.ru", "test")
    autorization_page.click_on_the_button()
    main_title = autorization_page.authorization_correct()
    assert main_title.is_displayed()
    assert main_title.text == 'Добро пожаловать!'


def test_2(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@protei.com", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_3(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@protei.ru", "TEST")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_4(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("TEST@protei.ru", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_5(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@PROTEI.ru", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_6(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@protei.RU", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_7(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email()
    assert wrong_password.is_displayed()


def test_8(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("test@protei.ru", "")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()


def test_9(browser):
    autorization_page = SearchHelper(browser)
    autorization_page.go_to_site()
    autorization_page.enter_login_pswd("TEST@PROTEI.RU", "test")
    autorization_page.click_on_the_button()
    wrong_password = autorization_page.incorrect_email_or_pass()
    assert wrong_password.is_displayed()

