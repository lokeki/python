# if/elif

#wyk

# age = 18
# isDrunk = False
# isRestctedArea = True
#
# if age < 18:
#     print("You are too young to buy alcohol")
# elif isDrunk:
#     print("You\'re drunk, we can\'t sell you alcohol")
# elif isRestctedArea:
#     print("Restricted area. Alcochol is forbidden")
# else:
#     print("Ok, you can buy alcohol")

#lab

minLikes = 500
minShares = 100
likes = 500#int(input())
shares = 100#int(input())

if likes >= minLikes and shares >= minShares:
    print('GREAT! Today our prizes drop 10% !!!')
elif likes < minLikes:
    print('We still need more likes to start the promotion')
else:
    print('We still need more shares to start the promotion')

isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
elif isWeekend:
    print('Come back on non-Weekend day')
else:
    print('You need to order Pizza or Big drink to have a Burger coupon')