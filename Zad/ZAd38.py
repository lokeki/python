import math

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # a1 - domyślna wartośc  2, oznacza pierwszy element ciągu,
    # factor - domyślna wartośc 2, oznacza współczynnik ciągu geometrycznego,
    # index - domyślna wartośc 2, oznacza  który element ciągu ma być wyliczony

    for element in range(1,index):
        print(element)
        value = a1 * math.pow(factor, element - 1)
        print(value)

GiveGeomSeqElement(3, 2, 10)
