import time

from selenium.webdriver.common.by import By


def test_guvi_LIVEClasses(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//p[text()='LIVE Classes']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//p[text()='LIVE Classes']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//p[text()='LIVE Classes']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//p[text()='LIVE Classes']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags and 'ul' in tags and 'dialog' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//p[text()='LIVE Classes']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'svg' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//p[text()='LIVE Classes']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'form' in tags and 'label' in tags and 'path' in tags and 'svg' in tags and 'option' in tags and 'select' in tags and 'input' in tags and 'label' in tags and 'span' in tags and 'details' in tags and 'img' in tags and 'a' in tags

def test_guvi_Courses(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//p[text()='Courses']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//p[text()='Courses']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//p[text()='Courses']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//p[text()='Courses']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags and 'ul' in tags and 'dialog' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//p[text()='Courses']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'svg' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//p[text()='Courses']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'form' in tags and 'label' in tags and 'path' in tags and 'svg' in tags and 'option' in tags and 'select' in tags and 'input' in tags and 'label' in tags and 'span' in tags and 'details' in tags and 'img' in tags and 'a' in tags

def test_guvi_Practice(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//p[text()='Practice']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//p[text()='Practice']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//p[text()='Practice']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//p[text()='Practice']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags and 'ul' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//p[text()='Practice']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'svg' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//p[text()='Practice']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'path' in tags and 'svg' in tags and 'input' in tags and  'span' in tags and 'img' in tags

def test_guvi_Resources(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//p[text()='Resources']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//p[text()='Resources']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//p[text()='Resources']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//p[text()='Resources']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags and 'ul' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//p[text()='Resources']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'svg' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//p[text()='Resources']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'form' in tags and 'label' in tags and 'path' in tags and 'svg' in tags and 'option' in tags and 'select' in tags and 'input' in tags and 'label' in tags and 'span' in tags and 'details' in tags and 'img' in tags and 'a' in tags


def test_guvi_Our_Products(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//p[text()='Our Products']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//p[text()='Our Products']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//p[text()='Our Products']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//p[text()='Our Products']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags and 'ul' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//p[text()='Our Products']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'svg' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//p[text()='Our Products']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags  and 'path' in tags and 'svg' in tags and 'input' in tags and 'span' in tags and 'img' in tags

def test_guvi_Loginbutton(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//*[@id='login-btn']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//*[@id='login-btn']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//*[@id='login-btn']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//*[@id='login-btn']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//*[@id='login-btn']/following-sibling::*"))
    assert len(all_following_siblings) > 0
    tags=[element.tag_name for element in all_following_siblings]
    assert 'button' in tags
    time.sleep(2)
    all_preceding_elements=(driver.find_elements(By.XPATH, "//*[@id='login-btn']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'path' in tags and 'svg' in tags and 'span' in tags and 'img' in tags

def test_guvi_SignUpbutton(driver):
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    parent_element=(driver.find_element(By.XPATH,"//button[text()='Sign up']/.."))
    assert parent_element.tag_name == "div"
    time.sleep(2)
    first_child_element = (driver.find_elements(By.XPATH, "//button[text()='Sign up']/child::*[1]"))
    assert len(first_child_element) == 0
    time.sleep(2)
    second_sibling=(driver.find_elements(By.XPATH,"//button[text()='Sign up']/following-sibling::*[2]"))
    assert len(second_sibling)== 0
    time.sleep(2)
    parent_of_href = (driver.find_element(By.XPATH, "//link[contains(@href,'manifest')]/parent::*"))
    assert parent_of_href.tag_name== 'head'
    time.sleep(2)
    all_ancestor_elements = (driver.find_elements(By.XPATH, "//button[text()='Sign up']/ancestor::*"))
    assert len(all_ancestor_elements) > 0
    tags = [element.tag_name for element in all_ancestor_elements]
    assert "html" in tags and "body" in tags and "header" in tags and 'div' in tags and 'main' in tags
    time.sleep(2)
    all_following_siblings = (driver.find_elements(By.XPATH, "//button[text()='Sign up']/following-sibling::*"))
    assert len(all_following_siblings) ==0
    all_preceding_elements=(driver.find_elements(By.XPATH, "//button[text()='Sign up']/preceding::*"))
    assert len(all_preceding_elements) > 0
    tags = [element.tag_name for element in all_preceding_elements]
    assert 'p' in tags and 'div' in tags and 'span' in tags and 'button' in tags and 'path' in tags and 'svg' in tags and 'span' in tags and 'img' in tags












