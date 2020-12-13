#generator zazwyczaj się używa kiedy jest duza baza danych
'''
listA = list(range(6))
listaB = list(range(6))

print(listA, listaB)

product = []

for a in listA:
    for b in listA:
        product.append((a,b))

print(product)

#skrocona wersja z ifem (lista)
product = [(a,b) for a in listA for b in listaB if a % 2 != 0 and b % 2 == 0]
print(product)

#wersja ze slownikiem, zmiana nawiasow kawadratowych na klamrowe, zmiana w zapisie danych
#zamiast (a,b), to a:b
product = { a:b for a in listA for b in listaB if a % 2 != 0 and b % 2 == 0}
#klucz (a) zosal a dane (b) sie zmienialy
print(product)

print('-' * 30)
#generator nie zajmuje pamięci jak lista, nie jest to gotowa np lista, nie przechowuje danych,
# przechowuje raczej metode, sposob na wygenerowanie tych danych
gen = ((a,b) for a in listA for b in listaB if a % 2 != 0 and b % 2 == 0)
print(gen)

print('-' * 30)
#zwraca i usuwa
print(next(gen))
print(next(gen))
print('-' * 30)
for x in gen:
    print(x)

print('-' * 30)
gen = ((a,b) for a in listA for b in listaB if a % 2 != 0 and b % 2 == 0)

#wyłapanie konca generatora poprzez try/except
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("All values have been generated")
        break
'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((port1, port2) for port1 in ports for port2 in ports if port1 < port2)
line = 0
while True:
    try:
        print(next(routes))
        line += 1
    except StopIteration:
        print("All values have been generated. It have been", line)
        break