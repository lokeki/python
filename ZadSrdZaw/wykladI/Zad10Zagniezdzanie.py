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
'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

linePorts = [(port1, potr2) for port1 in ports for potr2 in ports]
print(len(linePorts))

linePorts = [(port1, potr2) for port1 in ports for potr2 in ports if port1 != potr2]
print(len(linePorts))
