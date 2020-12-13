# mat
# percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
#            2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
#            3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
#            4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
#            8.740978348,6.174819567]
#
# countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
#              'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
#              'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
#              'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
#              'Cyprus','Italy']
#
# sumOfPoints = 4988
#
# print(min(percent), max(percent))
# for country in range(len(percent)):
#     print("Procenty:",percent[country])
#     print("Int:",int(percent[country]))
#     print("Zaokraglenie:",round(percent[country],2))
#     print("Punkty:",sumOfPoints*(percent[country]/100))
#     print(countries[country])

#modul math

import math
degree = 360

print((math.pi * degree)/180)

print(math.radians(degree))

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2

print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')
