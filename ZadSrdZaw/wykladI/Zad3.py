#automatyczna konwersja do typu logicznego

#jesli w napisie jest cos, to zawsze jest prawda

isOK = 'KUKU'
print(isOK, type(isOK))
if isOK:
    print("TRUE")

#jesli napis jest pusty, to jest to falsz

isOK = ''
print(isOK, type(isOK))
if isOK:
    print("TRUE")

# jesli int jest !=0, to jest to prawda

isOK = 50
print(isOK, type(isOK))
if isOK:
    print("TRUE")

# jesli int jest == 0, to jest to falsz

isOK = 0
print(isOK, type(isOK))
if isOK:
    print("TRUE")

# jesli lista nie jest pusta, to jest to prawda

isOK = [1,2,3]
print(isOK, type(isOK))
if isOK:
    print("TRUE")

# jesli lista jest pusta, to jest to falsz

isOK = []
print(isOK, type(isOK))
if isOK:
    print("TRUE")

#lab

def WriteDecision (listDecision):
    for position in range(len(listDecision)):
        print('{} - {}'.format(position + 1, listDecision[position]))

decision = ['load data', 'export data', 'analyze & predict']

while True:
    WriteDecision(decision)
    decisionUser = input("Your decision:")

    if not decisionUser:
        break

    if int(decisionUser):
        decisionUser = int(decisionUser) - 1
        if 0 < decisionUser < len(decision):
            print(decisionUser + 1, decision[decisionUser])
        else:
            print("This option is bad")
    else:
        print("You decision isn\'t a number.")
print("The program is over")

#z wyk

def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i + 1, options[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
options = ['load data', 'export data', 'analyze & predict']

while choice:

    choice = DisplayOptions(options)

    # executed only if something was entered
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')