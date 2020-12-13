'''
class Car:

    def __init__(self, brand, model, isOnSale):

        print(">>>> Class Car - init - starting")
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = "{} {}".format(brand, model)
        print(">>>> Class Car - init - finishing")

    def GetInfo(self):

        print(">>>> Class Car - GetInfo - starting")
        super().GetInfo()
        print("{} {}".format(self.brand, self.model).upper())
        print("Is On Sale {}".format(self.isOnSale))
        print(">>>> Class Car - GetInfo - finishing")

class Specialist:

    def __init__(self, firstName, lastName, brand):

        print(">>>> Class Specialist - init - starting")
        self.firstName = firstName
        self.lastName = lastName
        self.name = "{} {}".format(firstName, lastName)
        self.brand = brand
        print(">>>> Class Specialist - init - finishing")

    def GetInfo(self):

        print(">>>> Class Specialist - GetInfo - starting")
        print("{} {} - ({})".format(self.firstName, self.lastName, self.brand))
        print(">>>> Class Specialist - GetInfo - finishing")

class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstName, lastName):

        print(">>>> Class CarSpecialist - init - starting")
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstName, lastName, brand.upper())
        print(">>>> Class CarSpecialist - init - finishing")

    def GetInfo(self):

        print(">>>> Class CarSpecialist - GetInfo - starting")
        super().GetInfo()
        print(">>>> Class CarSpecialist - GetInfo - finishing")

tom = CarSpecialist("Toyota", "Corolla", True, "Tom", "Smith")
print(vars(tom))

tom.GetInfo()

print(CarSpecialist.__mro__)
'''

from datetime import date
from datetime import timedelta


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


class Promo():

    def __init__(self, name, discount, start_date, end_date, minimal_order):
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


class PromoCake(Cake, Promo):

    def __init__(self, cake, promo):

        Cake.__init__(self, cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
        Promo.__init__(self, promo.name, promo.discount, promo.start_date, promo.end_date, promo.minimal_order)


cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake.show_info()

promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
print(promo10.full_name)

promoCake = PromoCake(cake, promo10)
promoCake.show_info()
print(promoCake.full_name)

