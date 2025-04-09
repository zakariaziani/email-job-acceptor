import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = "zakariaziani99@gmail.com"
SUBJECT_PATTERN = "Job offer from ProZ.com Inc."
LINK_PATTERN = "https://cloud.protemos.com/tender/"
BUTTON_TEXT = "claim"
RUN_EVERY_SECONDS = 15

PROTEMOS_USERNAME = os.getenv("PROTEMOS_USERNAME")
PROTEMOS_PASSWORD = os.getenv("PROTEMOS_PASSWORD")