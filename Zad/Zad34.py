# wyk/random/prz

import random

myNumbers = []

while len(myNumbers) < 7:
    newNumber = random.randint(1,49)
    if newNumber in myNumbers:
        continue

    myNumbers.append(newNumber)

print(myNumbers)

#lab

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:
    for figure in figures:
        allCards.append(color + "-" + figure)

print(allCards)

random.shuffle(allCards)

print(allCards)

player1 = []
player2 = []

maxCatrs = len(allCards)

for cart in range(maxCatrs - 1):
    if cart % 2 == 0:
        player1.append(allCards[cart])
    else:
        player2.append(allCards[cart])

print("Player2:", player2)
print("Player1:", player1)
print('')

player1 = allCards[:12]
player2 = allCards[12:]

print("Player1:", player1)
print("Player2:", player2)


