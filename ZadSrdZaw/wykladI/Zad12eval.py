#eval/ pobranie kawalka kodu i uruchomienie/
# pozwala jednak wykonac tylko wyrazenia
# przyjmuje tylko jedną lionijke tekstu
'''
varX = 10
password = "My super secret password"

source = "varX + 2"

result = eval(source)
print(result)

'''

import math


while True:
    try:
        formula = input("Please enter a formula, use 'x' as the argument: ")

        if formula == '':
            break

        x = int(input("Please enter a x: "))
        print("x =", x, " ", formula, "=", round(eval(formula), 1))

    except ValueError:
        print("You must enter number")
        continue

    finally:
        print("Program is over")

