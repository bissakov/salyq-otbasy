import json
import os
from datetime import date
from os.path import join

import dotenv
import requests
from requests.adapters import HTTPAdapter
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

dotenv.load_dotenv()

# URLS
BASE_URL: str = os.getenv('BASE_URL')
INDEX_PAGE_URL: str = urljoin(BASE_URL, 'knp/main/index')
LOGOUT_URL: str = urljoin(BASE_URL, 'sonoweb/content/exit.faces')
NOTIFICATION_URL: str = urljoin(BASE_URL, 'knp/notifications/esutd/?id=')
TAX_STATEMENTS_URL: str = urljoin(BASE_URL, 'knp/declarations/registry/')

# SELECTORS
LOGIN_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'button.enter-by-cert-button')
AUTH_KEY_INPUT: tuple[str, str] = (By.CSS_SELECTOR, 'input.custom-file-input')
PASSWORD_INPUT: tuple[str, str] = (By.CSS_SELECTOR, 'input.listBox.form-control')
CONFIRM_PASSWORD_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'div.input-group-append > button')
CONFIRM_LOGIN_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'button.btn.btn-primary')
USER_INFO: tuple[str, str] = (By.CSS_SELECTOR, 'div.userInfo')
PAGE_TITLE: tuple[str, str] = (By.CSS_SELECTOR, 'h1.pageTitle')
NEWS_DATE: tuple[str, str] = (By.CSS_SELECTOR, 'div.news-item__date')
CALENDAR: tuple[str, str] = (By.CSS_SELECTOR, 'div.b-calendar')
MENU: tuple[str, str] = (By.CSS_SELECTOR, 'table.menuTable')
FROM_DATE_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'button#__BVID__44')
TO_DATE_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'button#__BVID__49')
SUBMIT_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, 'button[type="submit""]')
LOADER: tuple[str, str] = (By.CSS_SELECTOR, 'div.thin-loader')
NOTIFICATION_CONTENT: tuple[str, str] = (By.CSS_SELECTOR, '#notification-content')

# OTHER
TODAY = date.today().strftime('%d.%m.%Y')
with open(file=r'C:\Users\robot.ad\Desktop\Salyk\branch_mapping.json',
          mode='r', encoding='utf-8') as branch_mappings_file:
    BRANCH_MAPPINGS: dict[str, str] = json.load(branch_mappings_file)
# TODO Разкомментировать в случае ошибки с одним из филиалов,
# TODO чтобы робот не тратил время на ранние филиалы
# branch_mappings = {key: val for key, val in branch_mappings.items() if int(key) > 13}

# PATHS
SCREEN_LOCAL_FOLDER_PATH: str = join(r'C:\Users\robot.ad\Desktop\Salyk\screenshots', TODAY)
SCREEN_FSERVER_FOLDER_PATH: str = r'\\fserver\ДБУИО_Новая\ДБУИО_Общая папка' \
                                  r'\ДБУ_Информация УНУ\АКТ СВЕРКИ, ЛЧС\scrin-2023'
NOTIFICATION_FOLDER_PATH: str = join(r'C:\Users\robot.ad\Desktop\Salyk\notifications', TODAY)
BASE_PATH: str = r'\\dbu157\c$\ЭЦП ключи'
PDF_SAVE_PATH: str = r'\\fserver\ДБУИО_Новая\ДБУИО_Общая папка\ДБУ_Информация УНУ' \
                     r'\АКТ СВЕРКИ, ЛЧС\01_Анализ лицевых счетов\СПРАВКА об отсутсв зад-ти\2023'

# NETWORK
TOKEN, CHAT_ID = os.getenv('BOT_TOKEN'), os.getenv('CHAT_ID')
ERROR_TOKEN, ERROR_CHAT_ID = os.getenv('ERROR_TOKEN'), os.getenv('ERROR_CHAT_ID')

SESSION = requests.Session()
SESSION.mount('http://', HTTPAdapter(max_retries=5))


