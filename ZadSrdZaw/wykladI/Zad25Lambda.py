#lambda dowolna ilosc arg, jeden wyrazenie w srodku
'''
def double(x):

    return x * 2

x = 10
x = double(x)
print(x)

#lambda

x = 10
f = lambda x: x * 2
print(f(x))

def power (x,y):
    return x ** y

x = 5
y = 3
print(power(x,y))

f = lambda x,y: x ** y
print(f(x,y))

listNumbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]

def isOdd(x):
    return x % 2 != 0

print(isOdd(7), isOdd(2))

filterList = list(filter(isOdd, listNumbers))
print(filterList)

filterList = list(filter(lambda x: x % 2 != 0, listNumbers))
print(filterList)

print(list(filter(lambda x: x % 2 != 0, listNumbers)))


def generateMultiplyFunctions(n):
    return lambda x: n * x

nul2 = generateMultiplyFunctions(2)
nul3 = generateMultiplyFunctions(3)

print(nul2(12), nul3(8))
'''

textList = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)

listF = list(map(f, textList))
print(listF)

listF = list(map(lambda x: len(x), textList))
print(listF)