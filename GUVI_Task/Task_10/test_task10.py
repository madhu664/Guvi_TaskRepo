from selenium.webdriver.common.by import By
import time

def test_Negative_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("UnknownUser")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("WrongPassword")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(10)
    actual_message = driver.find_element(By.XPATH,"//h3[@data-test='error']").text
    expected_message = "Epic sadface: Username and password do not match any user in this service"
    assert actual_message == expected_message


def test_positive_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    print(driver.title)
    assert driver.title == "Swag Labs"

def test_positive_title_page(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    print(driver.title)
    assert driver.title == "Swag Labs"

def test_negative_title_page(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    print(driver.title)
    assert driver.title == "Swag"


def test_positive_current_page(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    print(driver.current_url)
    assert driver.current_url== "https://www.saucedemo.com/inventory.html"

def test_Negative_current_page(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    print(driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com/"

def test_extract_contents(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(10)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    with open("Webpage_task_11.txt", "w") as file:
        file.write(body_text)
