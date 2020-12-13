# interacja po slowniku
'''
workDays = [19, 21, 22, 21, 20, 22]
month = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthDays = dict(zip(month, workDays))
print(monthDays)

#przechodzimy po kluczach
for key in monthDays:
    print('Mon:', key, 'Day', monthDays[key])

#slownik.values() - wyswietlenie samych wartosci
for value in monthDays.values():
    print('Value is:', value)

'''

banknotesCoins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dictDenominations = {}
for value in banknotesCoins:
    dictDenominations[value] = 0

#print(dictDenominations)

dictDenominations[100] += 1
dictDenominations[20] += 1
dictDenominations[5] += 1
dictDenominations[0.5] += 1

dictDenominations[50] += 1
dictDenominations[20] += 2
dictDenominations[5] += 1
dictDenominations[2] += 2

dictDenominations[100] += 1
dictDenominations[50] += 1
dictDenominations[2] += 1

#formatowanie {0:6.2f} oznaczenie - 0; 6 znakow i 2 miejsca po przecinku f
for key in dictDenominations:
    print("Denomination: {0:6.2f} - amount {1:5}".format(key, dictDenominations[key]))