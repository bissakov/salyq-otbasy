from os import listdir
from os.path import join

import psutil
import win32com.client
from dataclasses import dataclass


def kill_all_processes(proc_name: str) -> None:
    for proc in psutil.process_iter():
        if proc_name in proc.name():
            process = psutil.Process(proc.pid)
            try:
                process.terminate()
            except psutil.AccessDenied:
                continue


@dataclass
class EmailInfo:
    attachments: str
    # recipient: str = 'robot.ad@hcsbk.kz'
    recipient: str = 'Zhangeldina.a@otbasybank.kz; kikimova.b@otbasybank.kz'
    subject: str = 'Уведомление с кабинета налогоплательщика'
    body: str = 'Уведомление с кабинета налогоплательщика филиала'


class Mail:
    def __init__(self, email_info: EmailInfo) -> None:
        kill_all_processes(proc_name='OUTLOOK.EXE')
        self.email = email_info
        try:
            self.outlook = win32com.client.Dispatch('Outlook.Application')
        except Exception:
            kill_all_processes(proc_name='OUTLOOK.EXE')
            self.outlook = win32com.client.Dispatch('Outlook.Application')

    def send(self):
        mail = self.construct_mail()
        mail.Send()
        self.outlook.Quit()

    def construct_mail(self):
        mail = self.outlook.CreateItem(0)
        mail.To = self.email.recipient
        mail.Subject = self.email.subject
        mail.Body = self.email.body
        if self.email.attachments:
            for attachment in self.email.attachments:
                mail.Attachments.Add(attachment)
        return mail


def send_email(folder_path: str):
    attachments = [join(folder_path, file_name) for file_name in listdir(folder_path)]
    if attachments:
        email_info = EmailInfo(attachments=attachments)
        Mail(email_info=email_info).send()


if __name__ == '__main__':
    send_email(folder_path=r'C:\Users\robot.ad\PycharmProjects\Salyk\Notifications\30.05.2023')
