import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://149.255.118.78:7080")
    yield driver
    driver.close()


# В классе определяем базовые методы для работы с WebDriver
class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://149.255.118.78:7080"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


# Класс для хранения локаторов
class SearchLocators:
    # Страница авторизации
    LOCATOR_SEARCH_LOGIN = (By.ID, "loginEmail")
    LOCATOR_SEARCH_PASSWORD = (By.ID, "loginPassword")
    LOCATOR_SEARCH_BUTTON = (By.ID, "authButton")
    # Панель всех разделов
    LOCATOR_NAVIGATION_BAR = (By.CSS_SELECTOR, "ul.uk-navbar-nav")
    # Раздел Варианты
    LOCATOR_MENU_MORE = (By.ID, "menuMore")
    LOCATOR_MENU_MORE_TITLE = (By.TAG_NAME, 'h3')
    # Раздел Главная страница
    LOCATOR_MENU_MAIN = (By.ID, "menuMain")
    LOCATOR_MENU_MAIN_TITLE = (By.TAG_NAME, 'h3')
    # Раздел Пользователи -> Таблица
    LOCATOR_MENU_USERS_OPENER = (By.ID, 'menuUsersOpener')
    LOCATOR_MENU_TABLE = (By.ID, 'menuUsers')
    LOCATOR_TABLE_TITLE = (By.XPATH, '//*[@id="addUser"]')
    # Раздел Пользователи -> Добавление
    LOCATOR_MENU_USERS_ADD = (By.CSS_SELECTOR, '#menuUserAdd')
    LOCATOR_USERS_ADD_TITLE = (By.XPATH, '//*[@id="inputsPage"]/form/fieldset/legend')
    # Поля раздела Пользователи -> Добавление
    LOCATOR_DATA_EMAIL = (By.ID, 'dataEmail')
    LOCATOR_DATA_PASSWORD = (By.ID, 'dataPassword')
    LOCATOR_DATA_NAME = (By.ID, 'dataName')
    LOCATOR_SELECT_GENDER = (By.ID, 'dataGender')
    LOCATOR_DATA_SELECT_11 = (By.ID, 'dataSelect11')
    LOCATOR_DATA_SELECT_12 = (By.ID, 'dataSelect12')
    LOCATOR_DATA_SELECT_21 = (By.ID, 'dataSelect21')
    LOCATOR_DATA_SELECT_22 = (By.ID, 'dataSelect22')
    LOCATOR_DATA_SELECT_23 = (By.ID, 'dataSelect23')
    LOCATOR_BUTTON = (By.ID, 'dataSend')
    LOCATOR_MESSAGE = (By.XPATH, '/html/body/div[3]/div/div[1]')
    LOCATOR_BUTTON_OK = (By.XPATH, '/html/body/div[3]/div/div[2]/button')
    # Поля пользователя в таблице
    LOCATOR_USER_EMAIL = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[10]/td[1]')
    LOCATOR_USER_NAME = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[10]/td[2]')
    LOCATOR_USER_GENDER = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[10]/td[3]')
    LOCATOR_USER_SELECT_1 = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[10]/td[4]')
    LOCATOR_USER_SELECT_2 = (By.XPATH, '//*[@id="dataTable"]/tbody/tr[10]/td[5]')
    LOCATOR_ALL_TABlE = (By.XPATH, '//*[@id="dataTable"]/tbody')

# Вспомогательные методы для работы с поиском
class SearchHelper(AuthorizationPage):

    def enter_login(self, login):  # Запись логина при авторизации
        search_field = self.find_element(SearchLocators.LOCATOR_SEARCH_LOGIN)
        search_field.click()
        search_field.send_keys(login)
        return search_field

    def enter_password(self, pswd):  # Запись пароля при авторизации
        search_field = self.find_element(SearchLocators.LOCATOR_SEARCH_PASSWORD)
        search_field.click()
        search_field.send_keys(pswd)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(SearchLocators.LOCATOR_SEARCH_BUTTON, time=5).click()

    def authorization_correct(self):
        return self.find_element(SearchLocators.LOCATOR_MENU_MAIN_TITLE, time=5)

    def check_navigation_bar(self):  # Проверка всех разделов в верхней панели
        all_list = self.find_elements(SearchLocators.LOCATOR_NAVIGATION_BAR, time=5)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu[0].split('\n')

    def check_menu_more(self):  # Проверка раздела ВАРИАНТЫ
        search_field = self.find_element(SearchLocators.LOCATOR_MENU_MORE)
        search_field.click()
        menu_more_text = self.find_element(SearchLocators.LOCATOR_MENU_MORE_TITLE)
        return menu_more_text

    def check_menu_main(self):  # Проверка раздела ГЛАВНАЯ СТРАНИЦА
        search_field = self.find_element(SearchLocators.LOCATOR_MENU_MAIN)
        search_field.click()
        menu_main_text = self.find_element(SearchLocators.LOCATOR_MENU_MAIN_TITLE)
        return menu_main_text

    def check_table(self):  # Проверка раздела Пользователи -> Таблица
        users_menu = self.find_element(SearchLocators.LOCATOR_MENU_USERS_OPENER)
        users_menu.click()
        table = self.find_element(SearchLocators.LOCATOR_MENU_TABLE)
        table.click()
        table_title_text = self.find_element(SearchLocators.LOCATOR_TABLE_TITLE)
        return table_title_text

    def check_users(self):  # Проверка раздела Пользователи -> Добавление
        users_menu = self.find_element(SearchLocators.LOCATOR_MENU_USERS_OPENER)
        users_menu.click()
        users_add = self.find_element(SearchLocators.LOCATOR_MENU_USERS_ADD)
        users_add.click()
        users_title_text = self.find_element(SearchLocators.LOCATOR_USERS_ADD_TITLE)
        return users_title_text

    def add_user(self, email, password, name):  # Проверка добавления пользователя
        users_menu = self.find_element(SearchLocators.LOCATOR_MENU_USERS_OPENER)
        users_menu.click()
        users_add = self.find_element(SearchLocators.LOCATOR_MENU_USERS_ADD)
        users_add.click()

        search_field_email = self.find_element(SearchLocators.LOCATOR_DATA_EMAIL)
        search_field_email.click()
        search_field_email.send_keys(email)

        search_field_password = self.find_element(SearchLocators.LOCATOR_DATA_PASSWORD)
        search_field_password.click()
        search_field_password.send_keys(password)

        search_field_name = self.find_element(SearchLocators.LOCATOR_DATA_NAME)
        search_field_name.click()
        search_field_name.send_keys(name)

        search_field_gender = Select(self.find_element(SearchLocators.LOCATOR_SELECT_GENDER))
        search_field_gender.select_by_visible_text("Мужской")

        search_field_radio_button = self.find_element(SearchLocators.LOCATOR_DATA_SELECT_12)
        search_field_radio_button.click()

        search_field_check_box = self.find_element(SearchLocators.LOCATOR_DATA_SELECT_21)
        search_field_check_box.click()

        button = self.find_element(SearchLocators.LOCATOR_BUTTON)
        button.click()

        search_message = self.find_element(SearchLocators.LOCATOR_MESSAGE)
        return search_message

    def check_user_in_table(self):  # Проверка наличия пользователя в таблице после добавления
        users_menu = self.find_element(SearchLocators.LOCATOR_MENU_USERS_OPENER)
        users_menu.click()
        table = self.find_element(SearchLocators.LOCATOR_MENU_TABLE)
        table.click()

        search_email = self.find_element(SearchLocators.LOCATOR_USER_EMAIL)
        search_name = self.find_element(SearchLocators.LOCATOR_USER_NAME)
        search_gender = self.find_element(SearchLocators.LOCATOR_USER_GENDER)
        search_selection_1 = self.find_element(SearchLocators.LOCATOR_USER_SELECT_1)
        search_selection_2 = self.find_element(SearchLocators.LOCATOR_USER_SELECT_2)

        list = [search_email, search_name, search_gender, search_selection_1, search_selection_2]
        return list

    def check_user_in_all_table(self):
        users_menu = self.find_element(SearchLocators.LOCATOR_MENU_USERS_OPENER)
        users_menu.click()
        table = self.find_element(SearchLocators.LOCATOR_MENU_TABLE)
        table.click()

        table = self.find_element(SearchLocators.LOCATOR_ALL_TABlE)
        return table


# Верхнеуровневая логика действий пользователя: авторизация + проверка Главной страницы
def test_1(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    main_title = authorization_page.authorization_correct()
    assert main_title.is_displayed()
    assert main_title.text == 'Добро пожаловать!'


# Проверка наличия всех разделов
def test_2(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    elements = authorization_page.check_navigation_bar()
    assert "АВТОРИЗАЦИЯ" in elements
    assert "ГЛАВНАЯ СТРАНИЦА" in elements
    assert "ПОЛЬЗОВАТЕЛИ" in elements
    assert "ВАРИАНТЫ" in elements


# Проверка текста в разделе Варианты
def test_3(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    menu_more_title = authorization_page.check_menu_more()
    assert menu_more_title.text == 'НТЦ ПРОТЕЙ'


# Проверка текста в разделе Таблица
def test_4(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    users_table_title = authorization_page.check_table()
    assert users_table_title.is_displayed()
    assert users_table_title.text == 'ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ'


# Проверка текста в разделе Пользователи
def test_5(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    users_add_title = authorization_page.check_users()
    assert users_add_title.text == 'Добавление пользователя'


# Проверка добавления пользователя
def test_6(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    user_adding = authorization_page.add_user('111@mail.ru', '222', 'qwerty')
    assert user_adding.text == 'Данные добавлены.'


# Проверка наличия добавленного пользователя в таблице
# (может не сработать, если таблица будет очищена, тогда придется указать новые XPATH к ячейкам таблицы)
def test_7(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()
    user_in_table = authorization_page.check_user_in_table()
    assert user_in_table[0].text == '111@mail.ru'
    assert user_in_table[1].text == 'qwerty'
    assert user_in_table[2].text == 'Мужской'
    assert user_in_table[3].text == '1.2'
    assert user_in_table[4].text == '2.1'


def test_8(browser):
    authorization_page = SearchHelper(browser)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_search_button()

    user_in_table = authorization_page.check_user_in_all_table()
    assert '111@mail.ru' in user_in_table
