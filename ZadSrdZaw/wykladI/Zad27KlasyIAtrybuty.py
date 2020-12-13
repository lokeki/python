#Klasy i atrybuty instancji klasy
'''
class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk


car01 = Car("Seat", "Ibiza", True, True, True)
car02  = Car("Opel", "Corsa", True, False, True)

print(car01.brand, car01.model, car01.isAirBagOk, car01.isPaintingOk, car01.isMechanicOk)
print(car02.brand, car02.model, car02.isAirBagOk, car02.isPaintingOk, car02.isMechanicOk)


'''

class Cake:

    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling

cake01 = Cake("Chocolade cake", "cake", "chocolade", ["chocolade", "eggs", "flour"], "chocolade" )
cake02 = Cake("Vanilia cookies", "cookies", "vanilia", ["chocolade", "vanilia", "eggs", "flour", "milk"], "" )

#print(cake01.name, cake01.kind, cake01.taste, cake01.addictions, cake01.filling)
#print(cake02.name, cake02.kind, cake02.taste, cake02.addictions, cake02.filling)

bakeryOffer = [cake01, cake02]

print("Today in our offer:")
for offer in bakeryOffer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(offer.name, offer.kind, offer.taste, offer.addictions, offer.filling))
