"""
If you get an SMTPAuthenticationError even when your password is correct,
it's possible that you have 2-factor authentication enabled.
You'll need to use an App Password to log in instead of your normal password.

If you don't have 2-FA enabled, you'll have to allow access by
less secure apps in your Gmail security preferences—though remember to deactivate
it once you've finished learning about sending e-mails with Python!
"""

import smtplib
from email.message import EmailMessage

email_content = ''' Dear Sir / madame

estoy enviando este correo desde python, esto es una prueba del curso.

Saludos
Renzo
'''

email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'you@egmail.com'
email['To'] = 'someoneelse@egmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('you@gmail.com', 'password')

smtp_connector.send_message(email)
smtp_connector.quit()