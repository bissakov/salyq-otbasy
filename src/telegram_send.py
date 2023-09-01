import logging

from config import TOKEN, ERROR_TOKEN, ERROR_CHAT_ID, CHAT_ID, SESSION


def _send_message(bot_token: str, chat_id: str, message: str) -> None:
    api_url = 'https://api.telegram.org/bot'
    SESSION.post(
        f'{api_url}{bot_token}/sendMessage',
        data={'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    )


def send_message(message: str, is_error: bool = False) -> None:
    bot_token, chat_id = (TOKEN, CHAT_ID) if not is_error else (ERROR_TOKEN, ERROR_CHAT_ID)
    try:
        _send_message(bot_token=bot_token, chat_id=chat_id, message=message)
    except Exception as e:
        logging.exception(f'Error while sending message to Telegram: {e}')
