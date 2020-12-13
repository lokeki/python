#wyklad/ operacje na plikach, wyrazenia logiczne
'''
import os

path = r'N:\temp\mydata.txt'

#os.remove(path)

if os.path.isfile(path):
    print("File %s is exists" % path)
else:
    print("Creating a file %s" % path)
    # 'x' jesli istnieje to zwróci blad
    open(path, 'x').close()
    print("File %s created" % path)


#result = os.path.isfile(path) or open(path, 'x').close()
#print(result)
'''

import os
import sys

def coutingValueInList (filePath):
    listFile = []
    try:
        if os.path.isfile(filePath):
            with open(filePath, 'r') as file:
                for line in file:
                    listFileFirst = line.split()
                    listFile += listFileFirst
            print(listFile)
            return len(listFile)
    except:
        print("Something went wrong", sys.exc_info()[0])

namePath = r'N:\temp\doKitu.txt'
lenList = coutingValueInList(namePath)
print(lenList)