#bledy
import sys

def textInList(ordersText):
    return ordersText.split('\n')

ordersText = '''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Pharma at grocery,Amoxicillin,?
Pharmacy 123,Cephalexin,100
Pharmacy 123,Prednisolone Sodium Phosphate
Pharma X,Nystatin,45'''

ordersList = textInList(ordersText)

file = r'N:\temp\orderss.txt'
with open(file, 'w') as fileOrders:

    for line in ordersList:
        line = line + '\n'
        fileOrders.write(line)

with open(file, 'r') as file:

     for line in file:

         line = line.replace('\n', '')
         order = line.split(',')

         try:
            pharmacyName = order[0]
            item = order[1]
            amount = int(order[2])

            print('Order from drugstore "%s", item "%s", amount %d' % (pharmacyName, item, amount))
            print()

         except ValueError as e:
             print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)
             print()

         except IndexError as e:
             print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)
             print()
         except:
             print('General error: ', sys.exc_info()[0])
             print()

print("Processing finished")
