#Klasa a instancja
'''
class Car:

    #zdefiniiwane na poziomie klsay
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsCarDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag ok {}".format(self.isAirBagOk))
        print("Painting ok {}".format(self.isPaintingOk))
        print("Mechanic ok {}".format(self.isMechanicOk))
        print("-" * 30)

print("Class level variables Before creating instances: ", Car.numberOfCars, Car.listOfCars)

car01 = Car("Seat", "Ibiza", True, True, True)
car02  = Car("Opel", "Corsa", True, False, True)

print("Class level variables Before creating instances: ", Car.numberOfCars, Car.listOfCars)

print(car01.brand, car01.model, car01.IsCarDamaged())
print(car02.brand, car02.model, car02.IsCarDamaged())


print(car01.brand, car01.model, car01.isAirBagOk, car01.isPaintingOk, car01.isMechanicOk)
print(car02.brand, car02.model, car02.isAirBagOk, car02.isPaintingOk, car02.isMechanicOk)

print("-" * 30)
car01.GetInfo()
car02.GetInfo()

print(vars(Car))
'''
class Cake:

    knownTypes = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakeryOffer = []

    def __init__(self, name, kind, taste, addictions, filling):

        self.name = name
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling
        if kind in self.knownTypes:
            self.kind = kind
        else:
            self.kind = 'other'
        self.bakeryOffer.append(self)

    def showInfo(self):

        print("{}".format(self.name).upper())
        print("Taste: {}".format(self.taste))
        if len(self.addictions) > 0:
            print("Addictions:")
            for addiction in self.addictions:
                print("\t",addiction)
        if self.filling:
            print("Filling: {}".format(self.filling))
        print("-" * 30)

    def setFilling(self, filling):

        self.filling = filling

    def addAdditives(self, additives):

        self.addictions.extend(additives)

cake01 = Cake("Chocolade cake", "cake", "chocolade", ["chocolade", "eggs", "flour"], "chocolade" )
cake02 = Cake("Vanilia cookies", "cookies", "vanilia", ["chocolade", "vanilia", "eggs", "flour", "milk"], "" )
cake03 = Cake("Muffin", "cookies", "vanilia", [], "")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

print(cake04.knownTypes)



print("Today in our offer:")
for offer in Cake.bakeryOffer:
    offer.showInfo()

cake02.setFilling("vanilia")
cake02.showInfo()

cake03.addAdditives(["flour", "milk", "chocolade"])
cake03.showInfo()

