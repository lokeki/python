#wysyłanie maila z pythona

import smtplib

mailFrom = "Your automation system"
mailTo = ['magazyn@gmail.com']
mailSubject = "Processing"
mailBody = '''
This is a tekst
Okej'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom,mailFrom,mailBody)

user = "name@gmail.com"
password = ']kokdo'

try:
    server = smtplib.SMTP_SSL("sntp.gmail.com", 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print("Message send")
except:
    print("Error")