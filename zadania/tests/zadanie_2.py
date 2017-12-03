from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.get("http://diabcontrol2.herokuapp.com/")
assert "DiabControl" in browser.title


def log_in(username, password):
    user_name = browser.find_element(By.ID, "id_username")
    user_name.send_keys(username)
    user_password = browser.find_element(By.ID, "id_password")
    user_password.send_keys(password)
    browser.find_element(By.NAME, "submit").click()


def go_to_patients_page():
    browser.find_element(By.LINK_TEXT, "My patients").click()
    # assert "My patients" in browser.find_element(By.CSS_SELECTOR, ".page-header")


def get_emails():
    emails = []
    for email in browser.find_elements(By.XPATH, "//td[@class='email']/a"):
        emails.append(email.text)
    print(emails)


log_in("doctor_a@example.com", "admin123")
assert "Doctor A" in browser.page_source
go_to_patients_page()
get_emails()
browser.close()
