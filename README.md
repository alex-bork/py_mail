# **ABORK_MAIL**
abork_mail is a module for sending emails easily.

## **1. Installation**

```command
pip intall abork_mail
```

## **2. Usage**

```python
from abork_mail.mail import SmtpMail
```

```python
mail = SmtpMail(par1=val1, par2=val2, ...)
mail.send()
```

Use the `mail_text_html` parameter instead of `mail_text` if you want to send HTML-content.
