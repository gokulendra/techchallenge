from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to fille the contact details form
def test_fill_contact(driver, contact_us_url):
    # Navigate to the Contact Us page
    driver.get(contact_us_url)

    # Wait for the form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contact-form")))

    marketing_dropdown = driver.find_element(By.ID, "contact-reason")  
    marketing_dropdown.send_keys("Marketing")
    message_field = driver.find_element(By.ID, "message")  
    message_field.clear()  
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

#To test the contact form
def test_contact_form_error_handling(contact_us_url):
    driver = webdriver.Chrome()

    try:
        test_fill_contact(driver, contact_us_url)

    finally:
        driver.quit()

contact_us_url = "https://www.tendable.com/contact"
test_contact_form_error_handling(contact_us_url)
