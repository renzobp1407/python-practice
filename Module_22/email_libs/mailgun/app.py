import requests

MAILGUN_API_URL = 'API_URL'
MAILGUN_API_KEY = 'API_key'

FROM_NAME = 'Jose'
FROM_EMAIL = 'jose@schoolofcode.me'

TO_EMAILS = ['jslvtr@gmail.com']
SUBJECT = 'Test email'
CONTENT = 'Hello, this is a email'

print(requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY), # basic auth
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }
))