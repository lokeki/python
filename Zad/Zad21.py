#for/range

for number in range(1,21):
    if number % 2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))

    #print(number)

#lab

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for dane in range(10):
    print(string_A)

print()
for dane in range(9):
   if dane % 2 == 0:
       print(string_A)
   else:
       print(string_B)

for dane in range(1,10):
    print(dane * 'x')

for dane in range(1,10):
   if dane % 2 == 0:
       print(dane * 'x')
   else:
       print(dane * 'o')
