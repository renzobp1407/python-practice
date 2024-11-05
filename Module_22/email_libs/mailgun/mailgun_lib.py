from mailgun_library import Mailgun

Mailgun.send_email(['test@gmail.com'], 
                   subject='Test email', 
                   content='this is a test email')