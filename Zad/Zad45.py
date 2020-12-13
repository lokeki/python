#bledy/else/finaly

import os
import sys

line = input("Price: ")

filePath = input('Podaj sciezke do pliku: ')
try:

    with open(filePath, 'w+') as file:
        file.write(line)

    line = int(line)
    print("The value saved in file is %d" % line)

except FileNotFoundError as e:
    print("Error opening file: ", sys.exc_info()[0])

except ValueError as e:
    print("The value entered cannot be converted to a number", sys.exc_info()[0])

except :
    print("SORRY - WE HAVE AN ERROR")

else:
    print("Actions completed successfully")
