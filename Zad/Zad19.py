#while

import random

#wyk
#
# cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
#
# boxCapacity = 90
# box = []
# i = 0

#my
# while i < len(cargo) and sum(box) <= boxCapacity:
#     if sum(box) + cargo[i] <= boxCapacity:
#         box.append(cargo[i])
#     i += 1
#
# print("The collected items sum is:", sum(box))
# print("The elements are:", box)
#
# box.clear()

#wyk
#
# i = 0
# cargo.sort()
# cargo.reverse()
# print(cargo)
#
# while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
#     if (boxCapacity - sum(box)) >= cargo[i]:
#         box.append(cargo[i])
#     i += 1
#
# print("The collected items sum is:", sum(box))
# print("The elements are:", box)

#lab

i = 0
maxNumber = 50

while i <= maxNumber - 1:
    wynik = i + (i + 1)
    i += 1
    print(wynik)

number = 1
previous_number = 0

while number <= 50:
    print(number + previous_number)
    previous_number = number
    number += 1

print("We start the game!")

myNumber = random.randint(0,20)
guess = int(input())
trials = 0

while guess != myNumber:
    if guess > myNumber:
        print("Sorry- my number is smaller than your guess, Try again!")
        guess = int(input())
        trials += 1
    else:
        print("Sorry- my number is greater than your guess, Try again!")
        guess = int(input())
        trials += 1
else:
    print("Congratulations, You WIN! Trilas:", trials)
