zad1 = (37 * 5 + 50) * 20 + 1020 - 1998
print(zad1)

obecnosc = input()
srednia = input()
praca = input()

print(obecnosc, ' ', srednia, ' ', praca)
if((float(obecnosc) >= 0.80 and float(srednia) >= 3.5) or praca == 'True'):
    print("Zaliczone")
else:
    print("Nie zaliczone")
