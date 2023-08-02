from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

a = 'folashade.adefiranye@arnergy.com'
b = 'Omowunmi16folashade'
# Replace 'your_username' and 'your_password' with the actual login credentials
email = a
password = b
PATH = r"C:\Users\Chris.Unwuchola\Downloads\chromedriver_win32 (2)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("https://solarbase.arnergy.com")

    # Find the username and password input fields and send keys
    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='email']")))
    email_input.send_keys(email)

    password_field= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))
    password_field.send_keys(password)

    # Press the login button
    login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'form-button')))
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(40)

    # Perform the search for "3.10"
    search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))
    search_box.send_keys("3.10")

    # Wait for the search results to load
    time.sleep(10)

    # Get the main-container element and print its text to the terminal
    main_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-container')))
    print("main-container")
    print(main_container.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
