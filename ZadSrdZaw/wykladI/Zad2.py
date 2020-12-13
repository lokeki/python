#typy zmienne mutable/ niezmienne immutable

days = ['mon','tue','wed','thu','fri','sat','sun']

#pracujemy na osobnej liscie, w innym miejscu w pamieci, zmieniamy dane tylko w jednej liscie
workdays = days.copy()
workdays.pop(-1)
workdays.pop(-1)
print(days)
print(workdays)

#pracujemy na liscie workdays i days, to samo miejsce w pamieci, dane zmieniaja sie w obu tabelach
workdays = days

# zmieniajac dane w zmiennej nastepuje zmiana jej id
a = 10
print(a, id(a))
a += 12
print(a, id(a))