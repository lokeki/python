#funkcje wartosci domyslne
'''
def BuyMe(prefix, what = "something nice"):
    print(prefix,what)

BuyMe("Please buy me", "a new car")
#nie wazna kolejnosc w przekazywaniu przez nazwe
BuyMe(what="a new car", prefix="Please buy me")
#bez argumentow, jesli w funkcji jest wartosc domyslna wartosci ktorej nie ma
BuyMe(prefix="Please buy me")

# jesli dla pierwszego jest domyslna to dla reszty tez musi

'''

def showProgress(howMany, character = "*"):
    print(character * howMany)


showProgress(10)
showProgress(15)
showProgress(30)

showProgress(10, '-')
showProgress(15, '+')