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

    ratio = float(input("New ratio: "))
    print(" The default % ratio for {} is {}, a new one is {}".format(myClient, clients[myClient], ratio))
    print("The costs for {} is {}".format(myClient, ratio * totalCost))
    print("New ratio a old ratio {}".format(clients[myClient] / ratio))

except KeyError as e:

    print("Clients {} is not on the list {}. \n Details: \n {}".format(myClient, [c for c in clients.keys()],e ))

except (ValueError, ZeroDivisionError) as e:

    print("There is a problem with entered value for ratio - it must be a number with '.' greater than 0. \n Detalis: \n {}".format(e))

#except ZeroDivisionError as e:

#    print("The new ratio can not be 0. \n Detalis: \n {}".format(e))

except Exception as e:

    print("Sorry we have an error... \n Detalis: \n {}".format(e))

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

except requests.exceptions.ConnectionError as e:

    print("Url is wrong. \n Details: \n {}".format(e))

except PermissionError as e:
    print("This file is ony to read. \n Details: \n {}".format(e))

except FileNotFoundError as e:

    print("This file dosen't exists. \n Details: \n {}".format(e))

except Exception as e:
    print("We have a error. Detalis: {}".format(e))

else:
    print("Succesful")

finally:
    print("Delect..")
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)

