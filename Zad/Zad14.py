#if

#wyk

# age = 27
#
# if age >= 18:
#     print("You are adult and you can buy alcohol")
# else:
#     print("You are too young to buy alcohol")
#
# isDrunk = False
#
# if age >= 18 and not isDrunk:
#     print("You are adult and you can buy alcohol")
# else:
#     print("Sorry, We can't sell you alcohol")
#
# isRestctedArea = False
#
# if age >= 18 and not isDrunk and not isRestctedArea:
#     print("You are adult and you can buy alcohol")
# else:
#     print("Sorry, We can't sell you alcohol")

# lab

MinLikes = 500
MinShare = 100
likes = 500#int(input())
shares = 100#int(input())

if likes >= MinLikes and shares >= MinShare:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    print('We still need more likes and shares to start the promotion')

isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get a coupon!")
else:
    print("If you buy pizza or big drink in week, you'll get a coupon!")

diskSize = 140
diskSizeUsed = 125
fileSize = 10

if diskSizeUsed + fileSize <= diskSize:
    print("File can be downloaded")
else:
    print("You don't have enough disk space!")