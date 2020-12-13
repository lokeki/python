'''
brandOnSale = "Opel"

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

    def __GetIsOnSale(self):

        return self.__isOnSale

    # medota instancji pierwszy argument self
    def __SetInOnSale(self, newInOnSaleStatus):

        if self.brand == brandOnSale:
            self.__isOnSale = newInOnSaleStatus
            print("Changing status InOnSale to {} for {}".format(newInOnSaleStatus, self.brand))
        else:
            print("Can't change status InOnSale. Sale value only for {}".format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetInOnSale, None, "if set to true, the car is available in sale/promo")

class Truck(Car):

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale, capacityKg):

        super().__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        #Car.__init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        #super(Truck, self).__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print("Capacity: {}".format(self.capacityKg))



truck01 = Truck("Ford", "Transit", True, False, True, False, 1600)
truck02 = Truck("Ford", "Transit", True, True, True, True, 1200)

print(truck01.brand, truck01.model, truck01.isAirBagOk, truck01.isPaintingOk, truck01.isMechanicOk, truck01.IsOnSale, truck01.capacityKg)
print(truck02.brand, truck02.model, truck02.isAirBagOk, truck02.isPaintingOk, truck02.isMechanicOk, truck02.IsOnSale, truck02.capacityKg)

truck02.GetInfo()
'''


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):

        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):

        super().show_info()
        print("Occasion: {}".format(self.occasion))
        print("Shape: {}".format(self.shape))
        print("Ornaments: {}".format(self.ornaments))
        print("Text: {}".format(self.text))

birthday = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',
                       'birthday', 'standard', 'hearts', '15')
wedding  = SpecialCake('Vanilla Cake','cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                       'wedding', 'pyramid', 'pigeons', 'Patricia & Tom')

birthday.show_info()
wedding.show_info()

for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()