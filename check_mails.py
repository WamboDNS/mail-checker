#!/home/denis/projects/mail-checker/.venv/bin/python

import os
import imapclient
import pyzmail
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv(os.path.join('TO_BE_REPLACED', '.env'))

# Set your email server and login credentials
EMAIL_SERVER = os.getenv('EMAIL_SERVER', 'imap.kit.edu')
EMAIL_ACCOUNT = os.getenv('EMAIL_ACCOUNT')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def clean_text(text):
    lines = text.splitlines()
    clean = [line.strip() for line in lines if line.strip()]
    return "\n".join(clean)

def fetch_unread_emails():
    # Connect to the email server
    server = imapclient.IMAPClient(EMAIL_SERVER, ssl=True)
    server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

    server.select_folder('INBOX', readonly=True)
    messages = server.search(['UNSEEN'])
    response = server.fetch(messages, ['BODY[]', 'FLAGS'])

    for msgid, data in response.items():
        email_message = pyzmail.PyzMessage.factory(data[b'BODY[]'])
        print(f"From: {email_message.get_address('from')[1]}")
        print(f"Subject: {email_message.get_subject()}")
        print(f"Received: {email_message.get('date')}\n\n")
        if email_message.text_part:
            body = email_message.text_part.get_payload().decode(email_message.text_part.charset)
            print(f"Body: {clean_text(body)[:100]}")
        elif email_message.html_part:
            body = email_message.html_part.get_payload().decode(email_message.html_part.charset)
            # Remove HTML tags for cleaner output (optional)
            soup = BeautifulSoup(body, 'html.parser')
            text = soup.get_text()
            print(f"Body: {clean_text(text)[:100]}")
        else:
            print("Body: (No text part found)")

        print("\n"+"=" * 75+"\n")

    server.logout()

def main():
    fetch_unread_emails()

if __name__ == "__main__":
    main()
