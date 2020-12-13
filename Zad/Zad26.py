#lab/dod/for

#zad1

# fibonacciIterations = 20
# number1 = 0
# number2 = 1
# number3 = 0
# for i in range(0,fibonacciIterations):
#     print(i, number3)
#     (number1, number2) = (number2, number3)
#     number3 = number1 + number2


#zad2
#
# text = '''Industrial Light & Magic: In this case, you find Python
#     used in the production process for scripting complex,
#     computer graphic-intensive films. Originally, Industrial
#     Light & Magic relied on Unix shell scripting, but it was
#     found that this solution just couldn’t do the job. Python
#     was compared to other languages, such as Tcl and Perl, and
#     chosen because it’s an easier-to-learn language that the
#     organization can implement incrementally. In addition, Python
#     can be embedded within a larger software system as a scripting
#     language, even if the system is written in a language such as
#     C/C++. It turns out that Python can successfully interact with
#     these other languages in situations in which some languages can’t.'''
#
# listOfText = text.replace("\n", ' ').split(' ')
# for word in listOfText:
#     if 'p' in word.lower():
#         print(word)

#zad3

# dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
#
# for diction in dictionary.keys():
#     print(diction, '-', dictionary[diction])

#zad4

text = '''Industrial Industrial industrial Light & Magic: In this case, you find Python
    used in the production process for scripting complex,
    computer graphic-intensive films. Originally, Industrial
    Light & Magic relied on Unix shell scripting, but it was
    found that this solution just couldn’t do the job. Python
    was compared to other languages, such as Tcl and Perl, and
    chosen because it’s an easier-to-learn language that the
    organization can implement incrementally. In addition, Python
    can be embedded within a larger software system as a scripting
    language, even if the system is written in a language such as
    C/C++. It turns out that Python can successfully interact with
    these other languages in situations in which some languages can’t.'''

listOfText = text.replace('\n', ' ').split(' ')
dictionary = {}
for word in listOfText:
    dictionary.setdefault(word, 0)
    dictionary[word] += 1
print(dictionary)
