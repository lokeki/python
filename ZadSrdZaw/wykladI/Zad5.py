import datetime
price = 123
bonus = 23
bonus_granted = True

# if bonus_granted:
#     price -= bonus
#
# print(price)
print(price - bonus) if bonus_granted else print(price)

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

todayWeekday = datetime.date.today().strftime('%A')
print(todayWeekday)