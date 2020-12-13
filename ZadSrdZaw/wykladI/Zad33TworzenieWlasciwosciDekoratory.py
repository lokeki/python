#Tworzenie Wlasciwosci za pomoca dekoratorow

'''
brandOnSale = "Opel"

class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        #wewnetrzne, schowane
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    # medota instancji pierwszy argument self
    def IsOnSale(self, newInOnSaleStatus):

        if self.brand == brandOnSale:
            self.__isOnSale = newInOnSaleStatus
            print("Changing status InOnSale to {} for {}".format(newInOnSaleStatus, self.brand))
        else:
            print("Can't change status InOnSale. Sale value only for {}".format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):

        self.__isOnSale = None

    @property
    def CarTitle(self):

        return "Brand: {}, Model: {}".format(self.brand, self.model).title()

car01 = Car("Seat", "Ibiza", True, True, True, False)
car02 = Car("Opel", "Corsa", True, False, True, True)

print(car01.IsOnSale)
#zwyczajnym przypipsaniem nie zmienimy danych
car01.IsOnSale = True

del car01.IsOnSale
print(car01.IsOnSale)

#nie mozna usunac, bez metody
#del car01.IsOnSale

print(car01.CarTitle)
'''


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
            print('>>>>>Text can be set only for cake ({})'.format(name))

        self.bakeryOffer.append(self)


    def showInfo(self):

        print("{}".format(self.name).upper())
        print("Kind:        {}".format(self.kind))
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

    @property
    def IsCakeText(self):

        return self.__text

    @IsCakeText.setter
    def IsCakeText(self, newText):

        if self.kind == 'cake' or self.kind == 'Cake':
            self.__text = newText
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    @IsCakeText.deleter
    def IsCakeText(self):
        self.__text = None



cake01 = Cake("Chocolade cake", "cake", "chocolade", ["chocolade", "eggs", "flour"], "chocolade" , True, "Wszystkiego naj")
cake02 = Cake("Vanilia cookies", "cookies", "vanilia", ["chocolade", "vanilia", "eggs", "flour", "milk"], "", True, "")
cake03 = Cake("Muffin", "cookies", "vanilia", [], "", True, "")
cake04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", False, "To nie tort")

print(cake01.IsCakeText)
cake01.showInfo()

cake01.IsCakeText = "Naj, naj, naj!!"
print(cake01.IsCakeText)
cake01.showInfo()

cake04.IsCakeText = "Chulaj"
print(cake04.IsCakeText)
cake04.showInfo()

'''print("Today in our offer:")
for offer in Cake.bakeryOffer:
    offer.showInfo()'''
