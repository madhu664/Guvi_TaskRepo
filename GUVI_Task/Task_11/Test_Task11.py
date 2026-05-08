from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


def test_positive_url_of_login_button(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    print(driver.current_url)
    assert driver.current_url== "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

def test_negative_url_of_login_button(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    print(driver.current_url)
    assert driver.current_url == "https://sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

def test_positive_username_password(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    username = driver.find_element(By.XPATH,"//*[@id='email']")
    time.sleep(10)
    assert username.is_displayed()
    assert username.is_enabled()
    username.send_keys("madhupriyaooty@gmail.com")
    password=driver.find_element(By.XPATH,"//*[@id='password']")
    time.sleep(10)
    assert password.is_displayed()
    assert password.is_enabled()
    password.send_keys("Halamma@123")

def test_negative_username_password(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    username = driver.find_element(By.XPATH, "//*[@id='email']")
    time.sleep(10)
    assert username.is_displayed()
    assert username.is_enabled()
    username.send_keys("maearg5y")
    actual_message = driver.find_element(By.XPATH,"//*[contains(text(),'email address')]").text
    expected_message = "Hmm...that doesnt look like an email address. Try again."
    assert actual_message == expected_message
    username.clear()
    username.send_keys("madhupriyaooty@gmail.com")
    password = driver.find_element(By.XPATH, "//*[@id='password']")
    time.sleep(10)
    password.send_keys("23")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-btn']")))
    time.sleep(10)
    login_button.click()
    time.sleep(10)
    actual_message = driver.find_element(By.XPATH,"//div[contains(text(),'Incorrect Email')]").text
    expected_message = "Incorrect Email or Password"
    assert actual_message == expected_message

def test_positive_submit_button(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    username = driver.find_element(By.XPATH,"//*[@id='email']")
    time.sleep(10)
    assert username.is_displayed()
    assert username.is_enabled()
    username.send_keys("madhupriyaooty@gmail.com")
    password=driver.find_element(By.XPATH,"//*[@id='password']")
    time.sleep(10)
    assert password.is_displayed()
    assert password.is_enabled()
    password.send_keys("Halamma@123")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-btn']")))
    time.sleep(10)
    login_button.click()
    time.sleep(10)
    actual_message = driver.find_element(By.XPATH,"//span[contains(text(),'Live Classes')]").text
    expected_message = "Live Classes + Placement Guidance"
    assert actual_message == expected_message

def test_negative_submit_button(driver):
    driver.get("https://www.guvi.in/")
    print(driver.current_url)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(10)
    username = driver.find_element(By.XPATH,"//*[@id='email']")
    time.sleep(10)
    assert username.is_displayed()
    assert username.is_enabled()
    username.send_keys("madhupriyaooty@gmail.com")
    password=driver.find_element(By.XPATH,"//*[@id='password']")
    time.sleep(10)
    assert password.is_displayed()
    assert password.is_enabled()
    password.send_keys("Halamma@123")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-btn']")))
    time.sleep(10)
    login_button.click()
    time.sleep(10)
    actual_message = driver.find_element(By.XPATH,"//span[contains(text(),'Live Classes')]").text
    expected_message = "No Live Classes + Placement Guidance"
    assert actual_message == expected_message


