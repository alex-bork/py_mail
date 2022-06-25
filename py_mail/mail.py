from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import smtplib


class IMail:

    def send(self):
        raise NotImplementedError('Method "send" not implemented.')


class SmtpMail(IMail):

    def __init__(self, 
                    smtp_host: str = None, 
                    smtp_port: int = None, 
                    smtp_user: str = None, 
                    smtp_password: str = None,
                    mail_subject: str = None,
                    mail_recipients: List = None,
                    mail_text: str = None,
                    mail_text_html: str = None):
      
        self.host = smtp_host
        self.port = smtp_port
        self.user = smtp_user
        self.password = smtp_password
        self.sender = smtp_user
        self.recipients = mail_recipients
        self.subject = mail_subject
        self.text = mail_text
        self.text_html = mail_text_html

    def send(self):

        self.__check_data()

        self.server = smtplib.SMTP(host=self.host, port=self.port)
        self.server.starttls()
        self.server.login(self.user, self.password)

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

        if not self.host or \
            not self.port or \
            not self.user or \
            not self.password or \
            not self.recipients or \
            not self.subject:
            raise ValueError('All of the following attributes have to be supplied: host, port, user, password, recipients, subject, text or text_html.')

        if self.text and self.text_html:
            raise ValueError('Supply either mail_text or mail_text_html')