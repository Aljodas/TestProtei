import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://149.255.118.78:7080")
    yield driver
    driver.close()


# Верный логин и пароль
def test_1(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@protei.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    main_title = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'h3')))
    assert main_title.is_displayed()
    assert main_title.text == 'Добро пожаловать!'


# Верный логин, неверный пароль
def test_2(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.ID, 'loginEmail')))
    login.send_keys('test@protei.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test1')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_password = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')))
    assert wrong_password.is_displayed()


# Неверный логин, верный пароль
def test_3(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test1@protei.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')))
    assert wrong_login.is_displayed()


# Пустой логин, верный пароль
def test_4(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный формат E-Mail")]')))
    assert wrong_login.is_displayed()


# Верный логин, пустой пароль
def test_5(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@protei.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')))
    assert wrong_login.is_displayed()


# Неверный логин (без protei), верный пароль
def test_6(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')))
    assert wrong_login.is_displayed()


# Неверный логин (mail вместо protei), верный пароль
def test_7(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'loginEmail')))
    login.send_keys('test@mail.ru')

    pswrd = driver.find_element(by=By.ID, value="loginPassword")
    pswrd.send_keys('test')

    button = driver.find_element(by=By.ID, value="authButton")
    button.click()

    wrong_login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Неверный E-Mail или пароль")]')))
    assert wrong_login.is_displayed()


