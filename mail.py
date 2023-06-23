from dataclasses import dataclass
from typing import List
from utils import dispatch, kill_all_processes


@dataclass
class EmailInfo:
    attachments: str
    # recipient: str = 'robot.ad@hcsbk.kz'
    recipient: str = 'Zhangeldina.a@otbasybank.kz; kikimova.b@otbasybank.kz'
    subject: str = 'Уведомление с кабинета налогоплательщика'
    body: str = 'Уведомление с кабинета налогоплательщика филиала'


def send_email(attachments: List[str]):
    kill_all_processes(proc_name='OUTLOOK.EXE')

    email_info = EmailInfo(attachments=attachments)
    with dispatch('Outlook.Application') as outlook:
        mail = outlook.CreateItem(0)
        mail.To = email_info.recipient
        mail.Subject = email_info.subject
        mail.Body = email_info.body
        if email_info.attachments:
            for attachment in email_info.attachments:
                mail.Attachments.Add(attachment)
        mail.Send()

