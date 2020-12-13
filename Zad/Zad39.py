def checkInt(number):
    if number[0] in ('-', '+'):
        return number[1:].isdigit()
    return number.isdigit()

a = input("Wprowadz liczbe a:")
b = input("Wprowadz liczbe b:")
c = input("Wprowadz liczbe c:")

if not(checkInt(a) and checkInt(b) and checkInt(c)):
    print("a, b and c need to be int!")
else:
    (a,b,c) = (int(a),int(b),int(c))

    if a == 0:
        print('a can not be 0!')
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = (-b)/(2 * a)
            print('x1 = ',x1)
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print('x1 = %f, x2 = %f' % (x1,x2))

