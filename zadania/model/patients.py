

class Patient:

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def go_to_patients_page():
        browser.find_element(By.LINK_TEXT, "My patients").click()
        assert "My patients" in browser.find_element(By.TAG_NAME, "h1")

# def get_patients_data():
#     patients = []
#     for patient in patients:
#