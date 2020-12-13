#Wprowadzenie do klas

'''
car1 = {
"carBrand" : "Seat",
"carModel" : "Ibiza",
"carIsAirBagOk" : True,
"carIsPaintinOk" : True,
"carIsMechanicOk" : True
}

car2 = {
"carBrand" : "Opel",
"carModel" : "Corsa",
"carIsAirBagOk" : True,
"carIsPaintinOk" : False,
"carIsMechanicOk" : True
}

def IsCarDamaged(aCar):

    return not (aCar["carIsAirBagOk"] and aCar["carIsPaintinOk"] and aCar["carIsMechanicOk"])

print(IsCarDamaged(car1))

print(IsCarDamaged(car2))

cars = [car1, car2]

for car in cars:
    print("{} {} damaged = {}".format(car["carBrand"], car["carModel"], IsCarDamaged(car)))

'''

cake1 = {
"taste" : 'vanilia',
"glaze" : 'chocolade',
"text" : 'Happy Brithday',
"weight" : 0.7
}

cake2 = {
"taste" : 'tee',
"glaze" : 'lemon',
"text" : 'Happy Python Coding',
"weight" : 1.3
}


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake["taste"], cake["glaze"], cake["text"], cake["weight"]))


cakes = [cake1, cake2]
for cake in cakes:

    show_cake_info(cake)
