'''
import random

class MemoryClass:

    listOfAlredySelectedItems = []

    def __init__(self, funct):
        print(">>>This is init of MemoryClass")
        self.funct = funct

    def __call__(self, list):

        print("This is call of MemoryClass instance")
        itemsNotSelected = [i for i in list if i not in MemoryClass.listOfAlredySelectedItems]
        print("+---- selecting only from list of", itemsNotSelected)
        item = self.funct(itemsNotSelected)
        MemoryClass.listOfAlredySelectedItems.append(item)
        return item


cars = ["Opel", "Toyota", "Fiat", "Ford", "Renault", "Mercedes", "BMW", "Peugeot", "Porsche", "Audi", "VW", "Mazda"]

@MemoryClass
def SelectTodayPromotion(listOfCars):

    return random.choice(listOfCars)

@MemoryClass
def SelectTodayShow(listOfCars):

    return random.choice(listOfCars)

@MemoryClass
def SelectFreeAccessoeirs(listOfCars):

    return random.choice(listOfCars)

print("Promotion:", SelectTodayPromotion(cars))
print("Show:", SelectTodayShow(cars),)
print("Free accessories:", SelectFreeAccessoeirs(cars))
'''

class MemoryClass:

    orderWithAdditives = []

    def __init__(self, funct):

        self.funct = funct

    def __call__(self, cake, listWithAdditives):

        orderWithAdditives = [newAdditive for newAdditive in listWithAdditives if newAdditive not in cake.additives]
        self.funct(cake, orderWithAdditives)

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

    def add_additives(self, additives):
        self.additives.extend(additives)

@MemoryClass
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts', 'coco'])
cake01.show_info()