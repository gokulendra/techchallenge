from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to verify Book A Demo
def verify_bookademo(driver, button_xpath):
    try:
        # Wait until the button is visible on the page (up to 10 seconds)
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, button_xpath))
        )
        if button.is_displayed() and button.is_enabled():
            print("The 'book-a-demo' button is present and visible on the UI.")
        else:
            print("The 'book-a-demo' button is either not visible or not clickable.")
    except Exception as e:
        print("Error: The 'book-a-demo' button was not found on the page. Exception:", e)

# Main function to load the website and check the button
def test_bookdemo_button(url):
    # Initialize WebDriver (ensure you have the correct path to your ChromeDriver)
    driver = webdriver.Chrome()

    try:
        # Open the URL
        driver.get(url)

        # Define the XPath for the "Request a Demo" button
        button_xpath = "/html/body/div[3]/div[2]/div[1]/nav/div[2]/a[2]"  # This assumes the button has this exact text

        # Call the function to verify the button
        verify_bookademo(driver, button_xpath)

    finally:
        driver.quit()

url = "https://www.tendable.com/"
test_bookdemo_button(url)
