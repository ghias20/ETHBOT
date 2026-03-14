import requests

BOT_TOKEN = "8616130804:AAFLglp4kVzcNTaKblxdzvXdMzrU-VTJ9rg"
CHAT_ID = "6538513650"

def send_message(text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=payload)