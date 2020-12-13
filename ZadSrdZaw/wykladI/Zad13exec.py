#exec nie zwraca wartosci
#przyjmuje wiele linijek tekstu

# varX = 10
# password = "My super secret password"
#
# #zmodyfikuje varX na 4
# source = "varX = 4"
# source = '''
# newVar = 1
# for i in range(varX):
#     print('-' * i)
#     newVar += 1
#     '''
#
# result = exec(source)
# print(result)
#
# print(varX)
# print(newVar)

import os

skryptList = [r"N:\tempExecEvel\skryptPierwszy.py", r"N:\tempExecEvel\skryptDrugi.py"]

for number in skryptList:
    if os.path.isfile(number):

        try:

            with open(number, 'r') as file:
                print(os.path.basename(number))
                exec(file.read())
                print('')

        except:
            print("Wrong")

    else:
        print("File dosn't existed")

