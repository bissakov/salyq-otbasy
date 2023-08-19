import os
from selenium.webdriver.common.by import By
from typing import Tuple
from urllib.parse import urljoin


BASE_URL: str = os.getenv('BASE_URL')
INDEX_PAGE_URL: str = urljoin(BASE_URL, 'knp/main/index')
LOGOUT_URL: str = urljoin(BASE_URL, 'sonoweb/content/exit.faces')
NOTIFICATION_URL: str = urljoin(BASE_URL, 'knp/notifications/esutd/?id=')
TAX_STATEMENTS_URL: str = urljoin(BASE_URL, 'knp/declarations/registry/')

LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'button.enter-by-cert-button')
AUTH_KEY_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, 'input.custom-file-input')
PASSWORD_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, 'input.listBox.form-control')
CONFIRM_PASSWORD_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'div.input-group-append > button')
CONFIRM_LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'button.btn.btn-primary')
USER_INFO: Tuple[str, str] = (By.CSS_SELECTOR, 'div.userInfo')
PAGE_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, 'h1.pageTitle')
NEWS_DATE: Tuple[str, str] = (By.CSS_SELECTOR, 'div.news-item__date')
CALENDAR: Tuple[str, str] = (By.CSS_SELECTOR, 'div.b-calendar')
MENU: Tuple[str, str] = (By.CSS_SELECTOR, 'table.menuTable')
FROM_DATE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'button#__BVID__44')
TO_DATE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'button#__BVID__49')
SUBMIT_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, 'button[type="submit""]')
LOADER: Tuple[str, str] = (By.CSS_SELECTOR, 'div.thin-loader')
NOTIFICATION_CONTENT: Tuple[str, str] = (By.CSS_SELECTOR, '#notification-content')

SCREEN_LOCAL_FOLDER_PATH: str = r'C:\Users\robot.ad\Desktop\Salyk\screenshots'
SCREEN_FSERVER_FOLDER_PATH: str = r'\\fserver\ДБУИО_Новая\ДБУИО_Общая папка' \
                                  r'\ДБУ_Информация УНУ\АКТ СВЕРКИ, ЛЧС\scrin-2023'
NOTIFICATION_FOLDER_PATH: str = r'C:\Users\robot.ad\Desktop\Salyk\notifications'
BASE_PATH: str = r'\\dbu157\c$\ЭЦП ключи'
PDF_SAVE_PATH: str = r'\\fserver\ДБУИО_Новая\ДБУИО_Общая папка\ДБУ_Информация УНУ' \
                     r'\АКТ СВЕРКИ, ЛЧС\01_Анализ лицевых счетов\СПРАВКА об отсутсв зад-ти\2023'
