
def ChengListColor(lenList, listOfColors):
    return listOfColors[:lenList]

def ColorInList (listOfColors):
    for number in range(len(listOfColors)):
        for number2 in range(len(listOfColors)):
            if number2 != number:
                print(listOfColors[number], ' - ', listOfColors[number2])
            else:
                continue

color = ["red", "orange", "green", "violet", "blue", "yellow"]

listOfColors = ChengListColor(3,color)
print(color)
print(listOfColors)
ColorInList(listOfColors)

corporation = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało 
szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym 
światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. 
W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do 
wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'''

print( corporation[corporation.index('(') + 1 : corporation.index(')')] )