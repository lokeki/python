'''
import csv
import types

#path - sciezka do pliku, ktory ma zostac utworzony
#header - lista naglowkow wartosci znajdujacych sie w pliku csv
#data - lista wartoisci ktr maj byc umieszczone w pliku
def exportToFileStatic(path, header, data):

    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print(">>>> This is function exportToFileStatic methond")

def exportToFileClass(cls, path):

    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["Brand", "Model", "IsOnSale"])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])

    print(">>>> This is function exportToFileClass methond")

def exportToFileInstance(self, path):

    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(["Brand", "Model", "IsOnSale"])
        writer.writerow([self.brand, self.model, self.IsOnSale])

    print(">>>> This is function exportToFileInstanc methond")

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

car01 = Car("Seat", "Ibiza", True, True, True, False)
car02 = Car("Opel", "Corsa", True, False, True, True)

print("Static--------------------" * 10)
Car.ExportToFileStatic = exportToFileStatic
#exportToFIleStatic(r"N:\klasyCSV\exportStatic.csv", ["Brand", "Model", "IsOnSale"],[car01.brand, car01.model, car01.IsOnSale])
Car.ExportToFileStatic(r"N:\klasyCSV\exportStatic.csv", ["Brand", "Model", "IsOnSale"],[car01.brand, car01.model, car01.IsOnSale])
print(dir(Car))

#Car.ExportToFileClass = exportToFIleClass
Car.ExportToFileClass = types.MethodType(exportToFileClass, Car)
Car.ExportToFileClass(r"N:\klasyCSV\exportClass.csv")
print(dir(Car))

car01.ExportToFileInstance = types.MethodType(exportToFileInstance, car01)
car01.ExportToFileInstance(path=r"N:\klasyCSV\exportInstance.csv")
print(dir(car01))

print("_" * 50)
# czy istnieje atrybut np.: "ExportToFileStatic" and callable - test czy mozemy wywolac ta funkcje
if hasattr(car01, "ExportToFileStatic") and callable(car01.ExportToFileStatic):
    print("The object has method ExportToFileStatic")
if hasattr(car01, "ExportToFileClass") and callable(car01.ExportToFileClass):
    print("The object has method ExportToFileClass")
if hasattr(car01, "ExportToFileInstance") and callable(car01.ExportToFileInstance):
    print("The object has method ExportToFileInstance")
'''

import types

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

def export_all_cake_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for c in cls.bakeryOffer:
            content = template.format(c.name, c.kind, c.taste, c.addictions, c.filling, "\n")
            f.write(content)
        print("Save")

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.addictions, self.filling, "\n")
        f.write(content)
        print("Save cake")


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



Cake.ExportAllCakeToHtml = types.MethodType(export_all_cake_to_html, Cake)
Cake.ExportAllCakeToHtml(r"N:\ZadHtml\cakes.html")

for c in Cake.bakeryOffer:
    c.ExportThisCakeToHtml = types.MethodType(export_this_cake_to_html, c)

for c in Cake.bakeryOffer:
   c.ExportThisCakeToHtml(r"N:\ZadHtml\{}.html".format(c.name.replace(" ", "_")))