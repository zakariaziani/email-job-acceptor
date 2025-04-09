import re
from bs4 import BeautifulSoup
import win32com.client
from config import SENDER_EMAIL, SUBJECT_PATTERN, LINK_PATTERN

def get_outlook_emails():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 = inbox
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)
    return messages

def find_matching_email():
    messages = get_outlook_emails()
    for message in messages:
        try:
            if SENDER_EMAIL in message.SenderEmailAddress and SUBJECT_PATTERN in message.Subject:
                body = message.HTMLBody
                link = extract_matching_link(body)
                if link:
                    print(f"Subject: {message.Subject}")
                    print(f"Link: {link}")
                    return link
        except AttributeError:
            continue
    return None

def extract_matching_link(html_body):
    soup = BeautifulSoup(html_body, "html.parser")
    for a in soup.find_all("a", href=True):
        if LINK_PATTERN in a["href"]:
            return a["href"]
    return None
