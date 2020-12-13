#wyk/zapisDoPliku

import os

webaddresses = []
# while True:
#     line = input("Wprowadz adres:")
#     if line == '' :
#         break
#     webaddresses.append(line)
#
# dirName = r'N:\temp'
# fileName = input("Wprowadz nazwe pliku:")
# path = os.path.join(dirName, fileName)
#
# with open(path,'w') as file:
#     for line in webaddresses:
#         line = line + '\n'
#         file.write(line)
# N:\temp\address.txt



while True:
    fileName = input("podaj sciezke dostepu:")

    if os.path.isfile(fileName):
        break
    print("Zla, podaj jeszcze raz")

with open(fileName,'r') as file:

    for line in file:
        webaddresses.append(line.replace('\n', ''))

for line in webaddresses:

    if line.endswith('.pl'):
        print("adres " + line + " jest adresem z polski")

        websPL = os.path.join(os.path.dirname(fileName), 'webs_pl.txt')
        lineInPolish = line + '\n'
        with open(websPL,'a') as filePolish:
            filePolish.write(lineInPolish)

    else:
        print("adres " + line + " nie jest adresem z Polski")

        websOther = os.path.join(os.path.dirname(fileName), 'webs_other.txt')
        lineInOther = line + '\n'
        with open(websOther,'a') as fileOther:
            fileOther.write(lineInOther)

print(webaddresses)



