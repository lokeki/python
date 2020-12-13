# funkcje z argumentami args i kwargs

# "*" w funkcji mowi że mozemy miec do czynienia z pewna lista dodatkowych
# elementow, ktore moga sie pojawic
# "**" argumenty poprzedzone nazwa (slowem kluczowym)
#wieksza ilosc argumentow
'''
def BuyMe(prefix, what = "something nice", *args, **kwatgs):
    print(prefix,what)
    print(args)
    print(kwatgs)

BuyMe("Please buy me", "a new car", "a cat", "a dog", "a dragon", shop = "mraket", color = "any")

products = ["milk", "bread", "flakes"]
parameters = {"price" : "low", "time" : "now"}

BuyMe("Buy me", "newspaper", *products, **parameters)
'''

def calculatePaint (efficencyLtrPerM2, *argumets):
    allArguments = sum(argumets)
    print(allArguments * efficencyLtrPerM2)

calculatePaint(3, 10, 10, 5)
listAgrum = [10, 10, 5]
calculatePaint(3, *listAgrum)

def logIt(pahtName, *arguments):
    try:
        with open(pahtName, 'a') as file:
            for argument in arguments:
                file.write(argument + " ")
            file.write("\n")

    except:
        print("Something was wrong")

logIt(r"N:\temp\zad16.txt",'Starting processing forecasting')
logIt(r"N:\temp\zad16.txt",'ERROR', 'Not enough data', 'invoices', '2020')


def log_it(*args):
    path = r'N:\temp\log_it.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')