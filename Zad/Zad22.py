#zagniezdzanie for

#wyk

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += '\t%3d' % (x*y)
    print(line)

#lab

i = 10#int(input())
wynik = 1
for dana in range(1,i+1):
    wynik *= dana
print(wynik)

for dana in range(1,11):
    wynik = 1
    for dane in range (1, dana+1):
        wynik *= dane
    print("Dana: ", dana, "\tWynik: ", wynik)


list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)