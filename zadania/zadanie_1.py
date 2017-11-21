from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("https://duckduckgo.com/")
assert "DuckDuckGo" in browser.title


def search_query():
    elem = browser.find_element(By.ID, "search_form_input_homepage")
    elem.clear()
    elem.send_keys("the biggest python software house")
    elem.send_keys(Keys.RETURN)


def go_to_first():
    best_python_house = WebDriverWait(browser, 10)\
        .until(EC.presence_of_element_located((By.XPATH, "//div[@id='r1-0']//a[@class='result__a']")))
    best_python_house.click()
    assert "STX Next" in browser.page_source

search_query()
go_to_first()
browser.close()
