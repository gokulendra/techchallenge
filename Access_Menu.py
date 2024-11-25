from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to test menu
def test_menu(driver, menu_name, menu_xpath):
    try:
        # Locate the menu by its XPath
        menu = driver.find_element(By.XPATH, menu_xpath)
        
        # Verify that the menu visibility
        if menu.is_displayed() and menu.is_enabled():
            print(f"Menu '{menu_name}' is accessible.")
        else:
            print(f"Menu '{menu_name}' is not accessible.")
    except Exception as e:
        print(f"Error accessing menu '{menu_name}': {e}")

# Main function to perform the testing
def test_website_menus(url):
    service = Service(ChromeDriverManager().install())  # Auto Chrome Driver
    
    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get(url)
        time.sleep(5)  
        # Test the accessibility of each menu by their XPath or CSS Selectors
        test_menu(driver, "About", "//a[text()='About']")
        test_menu(driver, "Products", "//a[text()='Products']")
        test_menu(driver, "Sectors", "//a[text()='Sectors']")
        test_menu(driver, "Contact", "//a[text()='Contact']")

    finally:
        driver.quit()

url = "https://www.tendable.com/"
test_website_menus(url)
