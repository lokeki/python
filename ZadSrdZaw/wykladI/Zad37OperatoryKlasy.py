'''
class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, accessories):

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accessories = accessories

    def GetInfo(self):

        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag ok {}".format(self.isAirBagOk))
        print("Painting ok {}".format(self.isPaintingOk))
        print("Mechanic ok {}".format(self.isMechanicOk))
        print("Accessories {}".format(self.accessories))
        print("-" * 30)

    def __iadd__(self, other):

        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMechanicOk, accessories)

        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMechanicOk, accessories)

        else:
            raise Exception("Adding type {} to Car is not implemeted".format(type(other)))

    def __add__(self, other):

        if type(other) is Car:
            return [self, other]

        else:
            raise Exception("Adding type {} to Car is not implemeted".format(type(other)))

    def __str__(self):
        return "Brand: {} Model: {}".format(self.brand, self.model)



car01 = Car("Seat", "Ibiza", True, True, True, ["winter tires"])
car01.GetInfo()

car01 += ["navigation system", "roof rack"]
car01.GetInfo()

car01 += "loudspeeker system"
car01.GetInfo()

car02 = Car("Opel", "Corsa", True, True, True, ["winter tires"])

carPack = car02 + car01
print("car 01 + car02", carPack[0].brand, carPack[1].brand)

print(car01)

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

    def __str__(self):

        return "Kind: {}  Name: {}  Additives: {}".format(self.kind, self.name, self.additives)

    def __iadd__(self, other):

        if type(other) is list:
            additives = self.additives.copy()
            additives.extend(other)
            '''
            albo
            self.additives.extend(other)
                return self
            '''
            return Cake(self.name, self.kind, self.taste, additives, self.filling)

        elif type(other) is str:
            additives = self.additives.copy()
            additives.append(other)
            '''
            albo
            self.additives.append(other)
                return self
            '''
            return Cake(self.name, self.kind, self.taste, additives, self.filling)

        else:
            raise Exception("Adding type {} to Car is not implemeted".format(type(other)))


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

cake01.show_info()
print(cake01)

cake01 += ['nutella', 'cookies']
cake01.show_info()
cake01 += "coco"
cake01.show_info()
cake01 += 1