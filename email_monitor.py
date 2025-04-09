from datetime import datetime, timedelta
import win32com.client
from bs4 import BeautifulSoup
from config import SENDER_EMAIL, SUBJECT_PATTERN, LINK_PATTERN, RUN_EVERY_SECONDS
import pytz

def find_matching_email():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 = inbox
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)
    tz_utc_plus_1 = pytz.FixedOffset(60)  # 60 minutes = 1 hour offset
    now = datetime.now().astimezone(tz_utc_plus_1)
    

    for message in messages:
        try:
            received_time = message.ReceivedTime
            received_time = received_time.replace(tzinfo=None)
            now = now.replace(tzinfo=None)

            delta = now - received_time

            # ✅ Only process emails received in the last 30 seconds
            if timedelta(seconds=0) <= delta <= timedelta(seconds=RUN_EVERY_SECONDS):

                if (SENDER_EMAIL.lower() in message.SenderEmailAddress.lower() and 
                    SUBJECT_PATTERN.lower() in message.Subject.lower()):
                    
                    body = message.HTMLBody
                    soup = BeautifulSoup(body, 'html.parser')
                    links = soup.find_all('a', href=True)

                    for link in links:
                        if LINK_PATTERN in link['href']:
                            print(f"📬 New matching email received at {received_time}")
                            return link['href']
        except Exception as e:
            print(f"⚠️ Error processing email: {e}")
            continue

    return None
