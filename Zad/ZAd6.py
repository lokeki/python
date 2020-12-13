name = "Jan"
age = 26
daysInYear = 365
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, age*daysInYear))

liczbaDzielona = 1234567890
dzielnik = 12345

print(liczbaDzielona, "divided by", dzielnik, "is", liczbaDzielona//dzielnik, "and the rest is", liczbaDzielona%dzielnik)