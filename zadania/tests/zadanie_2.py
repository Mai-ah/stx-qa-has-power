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
    assert "My patients" in browser.find_element(By.TAG_NAME, 'h1').text


def get_emails():
    emails = []
    for email in browser.find_elements(By.XPATH, "//td[@class='email']/a"):
        emails.append(email.text)
    return emails


def get_first_name():
    names = []
    for name in browser.find_elements(By.XPATH, "//td[@class='fname']"):
        names.append(name.text)
    return names


def get_last_name():
    last_names = []
    for last_name in browser.find_elements(By.XPATH, "//td[@class='lname']"):
        last_names.append(last_name.text)
    return last_names


log_in("doctor_a@example.com", "admin123")
assert "Doctor A" in browser.page_source
go_to_patients_page()
email = get_emails()
print(email)
browser.close()



