from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Replace these with your actual credentials
USERNAME = "your_website_username"
PASSWORD = "your_password"

# Path to the ChromeDriver executable
CHROMEDRIVER_PATH = "provide the path of chrome diver"

# URL of the website
URL = "website you want to automate,in this case it is coded for lms "

# Initialize the Chrome browser
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize the Chrome browser with the service
driver = webdriver.Chrome(service=ChromeService(CHROMEDRIVER_PATH), options=chrome_options)

def random_interaction(driver):
    try:
        # Find all interactive elements on the page, excluding assignment-related elements
        buttons = driver.find_elements(By.TAG_NAME, "button")
        links = driver.find_elements(By.TAG_NAME, "a")
        inputs = driver.find_elements(By.TAG_NAME, "input")

        # Filter out elements related to assignments
        buttons = [btn for btn in buttons if "assignment" not in btn.get_attribute("outerHTML").lower()]
        links = [link for link in links if "assignment" not in link.get_attribute("outerHTML").lower()]
        inputs = [input_field for input_field in inputs if "assignment" not in input_field.get_attribute("outerHTML").lower()]

        # Combine all interactive elements
        interactive_elements = buttons + links + inputs

        if interactive_elements:
            # Randomly select an element and click it
            element = random.choice(interactive_elements)
            try:
                element.click()
                print(f"Clicked element: {element.get_attribute('outerHTML')}")
            except Exception as e:
                print(f"Failed to click element: {e}")
    except Exception as e:
        print(f"Error in random_interaction: {e}")

def watch_video(driver):
    try:
        # Find video elements on the page
        videos = driver.find_elements(By.TAG_NAME, "video")
        if videos:
            # Randomly select a video and play it
            video = random.choice(videos)
            try:
                video.click()  # Simulate clicking the video to play it
                print(f"Playing video: {video.get_attribute('outerHTML')}")
            except Exception as e:
                print(f"Failed to play video: {e}")
    except Exception as e:
        print(f"Error in watch_video: {e}")

def open_pdf(driver):
    try:
        # Find PDF links on the page
        pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
        if pdf_links:
            # Randomly select a PDF link and open it
            pdf_link = random.choice(pdf_links)
            try:
                pdf_link.click()
                print(f"Opened PDF: {pdf_link.get_attribute('href')}")
            except Exception as e:
                print(f"Failed to open PDF: {e}")
    except Exception as e:
        print(f"Error in open_pdf: {e}")

try:
    # Open the website
    driver.get(URL)

    # Wait for the login page to load
    time.sleep(10)

    # Click the "Log In" button to trigger the modal
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log In')]"))
    )
    login_button.click()

    # Wait for the modal to appear
    time.sleep(5)

    # Wait for the username and password fields to be interactable
    username_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    password_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Find the login button inside the modal and click it
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(10)

    # Surf the website for 30 minutes
    start_time = time.time()
    while time.time() - start_time < 1800:  # 30 minutes = 1800 seconds
        # Randomly interact with elements on the page
        random_interaction(driver)

        # Watch videos if available
        watch_video(driver)

        # Open PDFs if available
        open_pdf(driver)

        # Scroll the page
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
        time.sleep(1)

except Exception as e:
    print(f"Error in main loop: {e}")

finally:
    # Keep the browser open for 5 minutes after the automation is complete
    time.sleep(300)
    driver.quit()