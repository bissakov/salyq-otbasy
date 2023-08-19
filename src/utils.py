import psutil
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


def kill_all_processes(proc_name: str) -> None:
    for proc in psutil.process_iter():
        if proc_name in proc.name():
            process = psutil.Process(proc.pid)
            try:
                process.terminate()
            except psutil.AccessDenied:
                continue
