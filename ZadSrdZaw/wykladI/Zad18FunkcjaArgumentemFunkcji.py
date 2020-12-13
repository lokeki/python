# Funkcja jako argument funkcji
'''
def Bake (what):
    print("Baking:", what)

def Add (what):
    print("Adding:",what)

def Mix (what):
    print("Mixing:", what)

cookBook = [(Add, "milk"), (Add, "eggs"), (Add, "flour"), (Add, "sugar"), (Mix, "ingerdients"), (Bake, "cookies")]

for activity, obj in cookBook:
    activity(obj)

print("-" * 40)

def Cook(activity, obj):
    activity(obj)

for activity, obj in cookBook:
    Cook(activity, obj)
'''


def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

def generateValues(nameFunctoin, parametrs):
    listWithResult = []

    for parametr in parametrs:
        listWithResult.append(nameFunctoin(parametr))
    return listWithResult


x_table = list(range(11))
print(type(x_table))

print(generateValues(double, x_table))
print(generateValues(root, x_table))
print(generateValues(negative, x_table))
print(generateValues(div2, x_table))
