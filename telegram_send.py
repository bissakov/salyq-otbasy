import os
import requests
from dotenv import load_dotenv


def _send_message(bot_token:str, chat_id: str, message: str) -> None:

    api_url = 'https://api.telegram.org/bot'

    send_message_url = f'{api_url}{bot_token}/sendMessage'

    params = {
        'chat_id': chat_id,
        'text': message
    }

    requests.post(send_message_url, data=params)


def send_message(message: str, is_error: bool = False) -> None:
    load_dotenv()
    bot_token, chat_id = (os.getenv('BOT_TOKEN'), os.getenv('CHAT_ID'))\
        if not is_error \
        else (os.getenv('ERROR_TOKEN'), os.getenv('ERROR_CHAT_ID'))
    _send_message(bot_token=bot_token, chat_id=chat_id, message=message)
    # pass
