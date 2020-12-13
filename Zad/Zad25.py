#lab/dod/while

# initialCapital = int(input("Capital:"))
# percent = 0.03
# maxTimeYears = int(input("Years:"))

#co miesiac

# for yeras in range(1,maxTimeYears + 1):
#     interest = 0
#     for ms in range(1,13):
#         interest += initialCapital * percent
#     initialCapital += interest
#     earnInterest += interest
#     print(initialCapital)

# co rok

# capital = initialCapital
# for year in range(1,maxTimeYears + 1):
#     capital = round((1 + percent)*capital, 2)
#     print("Yours capital is: ", capital, " Yours interest in:", round(capital - initialCapital,2))
#

#zad2
#
# intigerNumber = "20730906"
# numberSum = 0
#
# for number in range(len(intigerNumber)):
#     numberSum += int(intigerNumber[number])
# print(numberSum)
#
# number = int(intigerNumber)
# tempNumber = number
# sumNumber = 0
#
# while tempNumber > 0:
#     digit = tempNumber % 10
#     sumNumber += digit
#     tempNumber = tempNumber//10
# else:
#     print('the sum of digits of ', number, ' is', sumNumber)

#zad3

text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

listText = text.replace('\n', ' ').split(" ")
wordLenght = 6
quantity = 0
for position in listText :
    if position[-1].isalpha() and (len(position) > wordLenght):
        quantity += 1
        print(position)
    else:
        continue
print(quantity)