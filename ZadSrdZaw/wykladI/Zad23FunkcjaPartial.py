#Partial Funkacja

# import smtplib
# import functools
#
# def SendInfoEmail (user, password, mailFrom, mailTo, mailSubject, mailBody):
#     message = '''From: {}
#     Subject: {}
#
#     {}
#     '''.format(mailFrom,mailFrom,mailBody)
#     try:
#         server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#         server.ehlo()
#         server.login(user, password)
#         server.sendmail(user, mailTo, message)
#         server.close()
#         print("Message send")
#         return True
#     except:
#         print("Error")
#         return False
#
# mailFrom = "Your automation system"
# mailTo = ['magazyn@gmail.com']
# mailSubject = "Processing"
# mailBody = '''
# This is a tekst
# Okej'''
#
# message = '''From: {}
# Subject: {}
#
# {}
# '''.format(mailFrom,mailFrom,mailBody)
#
# user = "name@gmail.com"
# password = ']kokdo'
#
# SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject = 'Execution alter')
#
# SendInfoEmailFromGmail( mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

#SendInfoEmail (user, password, mailFrom, mailTo, mailSubject, mailBody)

import requests
import os
import functools

#pobieramy dane ze strony
def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


saveUrlToDir = functools.partial(save_url_file, dir = 'N:/temp/' , msg = "Please wait - the file {} will be downloaded")

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
#save_url_file(url, dir, file, msg)
saveUrlToDir(url = url, file = file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
#save_url_file(url, dir, file, msg)

saveUrlToDir(url = url, file = file)

