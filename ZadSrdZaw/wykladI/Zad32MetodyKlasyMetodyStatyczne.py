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

    #medota klasy pierwszy argument clasa - cls
    @classmethod
    def ReadFromText(cls, aText):
        # * przekazujemy osobne wartosci
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    #metoda statyczna nie ma zwiazku z klasa, nie ma specjalnych argumentow,
    # brak wspolnych metod i argumentow
    @staticmethod
    def ConvertKMKW(KM):

        return KM * 0.735

    @staticmethod
    def ConvertKWKM(KW):

        return KW * 1.36

lineOfText = "Renault:Megane:True:True:False:False"

car03 = Car.ReadFromText(lineOfText)
car03.GetInfo()

print("converting 120 KM to KW", Car.ConvertKMKW(120))
print("converting 90 KW to KM", Car.ConvertKWKM(90))

#car01 = Car("Seat", "Ibiza", True, True, True, False)
#car02 = Car("Opel", "Corsa", True, False, True, True)

'''

import pickle
import glob

class Cake:

    knownTypes = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakeryOffer = []

    def __init__(self, name, kind, taste, addictions, filling, glutenFree, text):

        self.name = name
        if kind in self.knownTypes:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling
        self.__glutenFree = glutenFree
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print("It isn't cake")

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
        if len(self.__text) > 0:
            print("Text:   {}".format(self.__text))
        print("-" * 30)

    def setFilling(self, filling):

        self.filling = filling

    def addAdditives(self, additives):

        self.addictions.extend(additives)

    def saveToFile(self, path):

        try:
            with open(path, 'wb') as file:
                pickle.dump(self,file)
        except:
            print("Something went wrong")

    @staticmethod
    def getBakeryFiles(nameDir):

        return glob.glob(nameDir)

    def __getText(self):

        return self.__text

    def __setText(self, newText):

        if self.kind == 'cake' or self.kind == 'Cake':
            self.__text = newText
        else:
            print("It isn't cake")

    IsCakeText = property(__getText, __setText, None, "This is cake and we write a text")

cake01 = Cake("Chocolade cake", "cake", "chocolade", ["chocolade", "eggs", "flour"], "chocolade" , True, "Wszystkiego naj")
cake02 = Cake("Vanilia cookies", "cookies", "vanilia", ["chocolade", "vanilia", "eggs", "flour", "milk"], "", True, "")
cake03 = Cake("Muffin", "cookies", "vanilia", [], "", True, "")
cake04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", False, "To nie tort")

cake01.saveToFile(r"N:\KlasyTemp\cake01.bakery")
cake02.saveToFile(r"N:\KlasyTemp\cake02.bakery")

print(Cake.getBakeryFiles(r"N:\KlasyTemp\*.bakery"))
'''
print("Today in our offer:")
for offer in Cake.bakeryOffer:
    offer.showInfo()
'''