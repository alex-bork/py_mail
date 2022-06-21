# **ABORK_MAIL**
abork_mail is a module for sending emails easily.

## **1. Installation**

```cmd
pip intall abork_mail
```

## **2. Usage**

```python
from abork_mail.mail import SmtpMail

SmtpMail(smtp_host="<smtp_host_address>",
                smtp_port=<smtp_port_number>,
                smtp_user="<sender_email>",
                smtp_password="<sender_password>",
                mail_recipients=["<recipient_email_address>"],
                mail_subject="<email_subject>",
                mail_text="<email_text>").send()
```

Use the "mail_text_html" instead of "mail_text" if you want to send HTML-content.
