import logging
import os
import requests


def _send_message(bot_token: str, chat_id: str, message: str) -> None:
    api_url = 'https://api.telegram.org/bot'
    requests.post(
        f'{api_url}{bot_token}/sendMessage',
        data={'chat_id': chat_id, 'text': message}
    )


def send_message(message: str, is_error: bool = False) -> None:
    bot_token, chat_id = (os.getenv('BOT_TOKEN'), os.getenv('CHAT_ID'))\
        if not is_error \
        else (os.getenv('ERROR_TOKEN'), os.getenv('ERROR_CHAT_ID'))
    try:
        _send_message(bot_token=bot_token, chat_id=chat_id, message=message)
    except Exception as e:
        logging.error(f'Error while sending message to Telegram: {e}')
    # pass


if __name__ == '__main__':
    send_message('test', is_error=True)
