#trojkatPascala

import random
numbers = [1]

print(numbers)

for i in range(5):
    newNumbers = [1]
    position = 0

    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position + 1])
        position += 1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    print(numbers)


# lab

# colors = ['Hearts','Diamonds','Clubs','Spades']
# figures = [
#     {'Figure':'Ace',  'Power':14},
#     {'Figure':'King', 'Power':13},
#     {'Figure':'Queen','Power':12},
#     {'Figure':'Jack', 'Power':11},
#     {'Figure':'10',   'Power':10},
#     {'Figure':'9',    'Power':9}]
#
# allCarts = []
# for color in colors:
#     print("1",color)
#     for figure in figures:
#         aCard = figure.copy()
#         aCard['Color'] = color
#         allCarts.append(aCard)
#
# print(allCarts)
#
# random.shuffle(allCarts)
#
# print(allCarts)
#
# player1 = allCarts[:12]
# player2 = allCarts[12:]
#
# print("Player1:", player1)
# print("Player2:", player2)
#
# while len(player2) > 0 or len(player1) > 0:
#     card1 = player1.pop()
#     print(card1)
#     card2 = player2.pop()
#     print(card2)
#
#     if card1['Power'] == card2 ['Power']:
#         player1.append(card1)
#         player2.append(card2)
#     elif card1['Power'] > card2 ['Power']:
#         player1.append(card1)
#         player1.append(card2)
#     else:
#         player2.append(card1)
#         player2.append(card2)
#
#     print("Player1:", player1)
#     print("Player2:", player2)
#
# if len(player2) > 0:
#     print("Wygrałeś player2! Ilosc kart:", len(player2))
# else:
#     print("Wygrałeś player1! Ilosc kart:", len(player1))