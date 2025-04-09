from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from config import BUTTON_TEXT

def open_browser_and_claim(link):
    options = Options()
    options.add_argument("--headless=new")  # Remove 'new' if you face issues
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(link)
        driver.implicitly_wait(10)

        # Look for a button with specific text
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if BUTTON_TEXT.lower() in button.text.lower():
                button.click()
                print("✅ Button clicked.")
                break
        else:
            print("❌ 'Claim' button not found.")
    finally:
        time.sleep(3)
        driver.quit()
