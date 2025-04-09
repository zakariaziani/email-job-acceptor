from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from config import PROTEMOS_USERNAME, PROTEMOS_PASSWORD, BUTTON_TEXT

def open_browser_and_claim(link):
    options = Options()
    # Remove headless for debugging:
    # options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    try:
        print("🌐 Opening link:", link)
        driver.get(link)
        driver.implicitly_wait(10)

        # Check if we're on the login page
        if "sign in" in driver.page_source.lower():
            print("🔐 Login required. Submitting credentials...")
            driver.find_element(By.NAME, "LoginForm[username]").send_keys(PROTEMOS_USERNAME)
            driver.find_element(By.NAME, "LoginForm[password]").send_keys(PROTEMOS_PASSWORD)
            driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()
            time.sleep(3)  # wait for login

        # Try to click the 'claim' button
        print("🔎 Looking for claim button...")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if BUTTON_TEXT.lower() in button.text.lower():
                button.click()
                print("✅ 'Claim' button clicked.")
                break
        else:
            print("❌ 'Claim' button not found.")

    except Exception as e:
        print("❗ Error during web automation:", e)
    finally:
        time.sleep(3)
        driver.quit()
