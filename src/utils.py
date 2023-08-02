import logging
import psutil
import pywinauto
import win32com.client as win32
from contextlib import contextmanager


@contextmanager
def dispatch(application: str) -> None:
    app = win32.Dispatch(application)
    if 'Outlook' not in application:
        app.DisplayAlerts = False
    try:
        yield app
    finally:
        app.Quit()


@contextmanager
def doc_open(app: win32.CDispatch, document: str, save: bool = True) -> None:
    app.Documents.Open(document)
    doc = app.ActiveDocument
    try:
        yield doc
    finally:
        doc.Close(save)


def kill_all_processes(proc_name: str) -> None:
    for proc in psutil.process_iter():
        if proc_name in proc.name():
            process = psutil.Process(proc.pid)
            try:
                process.terminate()
            except psutil.AccessDenied:
                continue


def get_current_process_pid(proc_name: str) -> int or None:
    return next((p.pid for p in psutil.process_iter() if proc_name in p.name()), None)


def close_microsoft_office_warning(app: pywinauto.Application) -> None:
    for win in app.windows():
        win_text = win.window_text()
        if not win_text:
            continue
        window = app.window(title=win_text)
        window['Закрыть'].click()
    logging.info(f'WINWORD.EXE license window closed')


def paste_notification_content(proc_name: str) -> None:
    app_pid = get_current_process_pid(proc_name=proc_name)
    logging.info(f'{proc_name} pid {app_pid}')
    app = pywinauto.Application(backend='uia').connect(process=app_pid)
    logging.info(f'{proc_name} app {app} is connected to {app_pid}')

    close_microsoft_office_warning(app=app)

    app.top_window().set_focus()
    logging.info(f'WINWORD.EXE top window is focused')

    app.top_window().type_keys('{VK_CONTROL down}v{VK_CONTROL up}')
    logging.info(f'Notification content is pasted')
