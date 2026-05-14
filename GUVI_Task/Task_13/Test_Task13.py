import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_drag_and_drop(driver):
    driver.get("https://jqueryui.com/droppable/")
    iframe=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
    driver.switch_to.frame(iframe)
    time.sleep(2)
    drag_element=driver.find_element(By.XPATH,"//*[@id='draggable']")
    drop_element=driver.find_element(By.XPATH,"//*[@id='droppable']")
    actions= ActionChains(driver)
    actions.drag_and_drop(drag_element,drop_element).perform()
    time.sleep(2)

def test_without_drag_and_drop(driver):
    driver.get("https://jqueryui.com/droppable/")
    iframe=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
    driver.switch_to.frame(iframe)
    time.sleep(2)
    drag_element=driver.find_element(By.XPATH,"//*[@id='draggable']")
    drop_element=driver.find_element(By.XPATH,"//*[@id='droppable']")
    actions= ActionChains(driver)
    actions.click_and_hold(drag_element).perform()
    actions.move_to_element(drop_element).perform()
    actions.release(drop_element).perform()
    time.sleep(2)

