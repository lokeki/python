'''
class MemoryClass:

    def __init__(self, list):
        self.listOfItems = list

#pozwala nam wywolac instancje jako funkcje
    def __call__(self, item):
        self.listOfItems.append(item)

mem = MemoryClass([])
print("List of items in memory", mem.listOfItems)

mem.listOfItems.append("buy sugar")
print("List of items in memory", mem.listOfItems)

mem("buy milk")
print("List of items in memory", mem.listOfItems)

mem("buy coffe")
print("List of items in memory", mem.listOfItems)

#callable czy może je teraz wywolywac
print("Thi class is callable:", callable(MemoryClass))
print("Thi class is callable:", callable(mem))
'''



class NoDuplicates:

    def __init__(self):

        self.listInClass = []

    def __call__(self, newItems):

        for i in newItems:
            if not i in self.listInClass:
                self.listInClass.append(i)

myNoDupList = NoDuplicates()
print(myNoDupList.listInClass)

myNoDupList(['keyboard','mouse'])
print(myNoDupList.listInClass)

myNoDupList(['keyboard','mouse','pendrive'])
print(myNoDupList.listInClass)

myNoDupList(['charger','pendrive'])
print(myNoDupList.listInClass)