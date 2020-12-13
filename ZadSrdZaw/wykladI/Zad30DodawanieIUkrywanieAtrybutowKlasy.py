# dodawanie i ukrywanie atrybutow klasy
'''
class Car:

    #zdefiniiwane na poziomie klsay
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        #wewnetrzne, schowane
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsCarDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag ok {}".format(self.isAirBagOk))
        print("Painting ok {}".format(self.isPaintingOk))
        print("Mechanic ok {}".format(self.isMechanicOk))
        print("Is On Sale {}".format(self.__isOnSale))
        print("-" * 30)

car01 = Car("Seat", "Ibiza", True, True, True, False)
car02  = Car("Opel", "Corsa", True, False, True, True)

print("-" * 30)
car01.GetInfo()
car02.GetInfo()

#stworzenie atrybutu
setattr(car02, 'Taxi', False)

#sprawdzenie czy taki atrybut istnieje
print(hasattr(car02, 'Taxi'))

#usuniecie atrybutu
delattr(car02, 'Taxi')
'''
class Cake:

    knownTypes = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakeryOffer = []

    def __init__(self, name, kind, taste, addictions, filling, glutenFree):

        self.name = name
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling
        self.__glutenFree = glutenFree
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
        print("Gluten free: {}".format(self.__glutenFree))
        print("-" * 30)

    def setFilling(self, filling):

        self.filling = filling

    def addAdditives(self, additives):

        self.addictions.extend(additives)

cake01 = Cake("Chocolade cake", "cake", "chocolade", ["chocolade", "eggs", "flour"], "chocolade" , True)
cake02 = Cake("Vanilia cookies", "cookies", "vanilia", ["chocolade", "vanilia", "eggs", "flour", "milk"], "", True)
cake03 = Cake("Muffin", "cookies", "vanilia", [], "", True)
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)

print(cake04.knownTypes)



print("Today in our offer:")
for offer in Cake.bakeryOffer:
    offer.showInfo()

'''
cake02.setFilling("vanilia")
cake02.showInfo()

cake03.addAdditives(["flour", "milk", "chocolade"])
cake03.showInfo()

'''

cake03.__glutenFree = False

cake03.showInfo()
print(dir(cake03))

cake03._Cake__glutenFree = False

print(dir(cake03))

cake03.showInfo()