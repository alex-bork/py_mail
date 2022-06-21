from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import smtplib


class IMail:

    def send(self):
        raise NotImplementedError('Method "send" not implemented.')


class SmtpMail(IMail):

    def __init__(self, 
                    smtp_host: str, 
                    smtp_port: int, 
                    smtp_user: str, 
                    smtp_password: str,
                    mail_subject: str,
                    mail_recipients: List,
                    mail_text: str = None,
                    mail_text_html: str = None):
      
        self.host = smtp_host
        self.port = smtp_port
        self.user = smtp_user
        self.passwword = smtp_password
        self.sender = smtp_user
        self.recipients = mail_recipients
        self.subject = mail_subject
        self.text = mail_text
        self.text_html = mail_text_html

    def send(self):

        self.__check_data()

        self.server = smtplib.SMTP(host=self.host, port=self.port)
        self.server.starttls()
        self.server.login(self.user, self.passwword)

        mail = MIMEMultipart()
        mail['From'] = self.sender
        mail['Subject'] = self.subject

        if self.text:
            mail.attach(MIMEText(self.text, 'plain'))
        else:
            mail.add_header('Content-Type', 'text/html')
            mail.set_payload(self.text_html)

        for recipient in self.recipients: 

            mail['To'] = recipient
            self.server.sendmail(self.sender, self.recipients, mail.as_string())

        self.server.quit()

    def __check_data(self):

        if self.text != None and self.text_html != None:
            raise ValueError('Supply either mail_text or mail_text_html')