from email_monitor import find_matching_email
from web_automation import open_browser_and_claim
import time

def main():
    print("🔁 Checking for new matching emails...")
    link = find_matching_email()
    if link:
        print("🌐 Opening browser and attempting to claim...")
        open_browser_and_claim(link)
    else:
        print("📭 No matching email found.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)  # Check every 60 seconds
