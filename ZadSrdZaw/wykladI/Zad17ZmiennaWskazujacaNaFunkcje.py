# zmienna wskazujaca na funkcje
'''
def BuyMe( what ):
    print(what)

BuyMe("a new car")

StealForMe = BuyMe

print(type(StealForMe))
StealForMe("a new car")
'''


def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number = 8

transformations = [double, root, div2, negative]

tmpReturnValue = number

for transformation in transformations:
    transformation(tmpReturnValue)
    print(tmpReturnValue)
    
print(number)