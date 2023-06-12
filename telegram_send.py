import os
from dotenv import load_dotenv
import requests


def _send_message(message: str) -> None:
    load_dotenv()

    api_url = 'https://api.telegram.org/bot'
    bot_token, chat_id = os.getenv('BOT_TOKEN'), os.getenv('CHAT_ID')

    send_message_url = f'{api_url}{bot_token}/sendMessage'

    params = {
        'chat_id': chat_id,
        'text': message
    }

    requests.post(send_message_url, data=params)


def send_message(message: str) -> None:
    _send_message(message=message)
    # pass

