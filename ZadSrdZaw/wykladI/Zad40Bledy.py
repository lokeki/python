'''clients = {
    "INFO" : 0.5,
    "DATA" : 0.2,
    "SOFT" : 0.2,
    "INTER" : 0.1,
    "OMEGA" : 0.0
}

myClient = input("Enter client's name: ")
totalCost = 7200

try:

    print(" The % ratio for {} is {}".format(myClient, clients[myClient]))

except Exception as e:

    print("Sorry we have an error... \n Detalis: \n {}".format(e))

else:

    print("The costs for {} is {}".format(myClient, clients[myClient] * totalCost))

finally:

    print("-= Calcutaion finiszed =-")
'''

import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'N:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)

    print("Dowloading..")
    save_url_to_file(url, tmpfile_path)

    print("Copy..")
    #kopiowanie pliku tmpfile_path do file_path
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print("We have a error. Detalis: {}".format(e))

else:
    print("Succesful")

finally:
    print("Delect..")
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)



