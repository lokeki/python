helloMessage = "Hello %s!"

print(helloMessage % 'Kate')
print(helloMessage %'Chirs')

helloMessage = "Hello {0:s}!"

print(helloMessage.format('Kate'))
print(helloMessage.format('Chirs'))

helloMessage = "%s has %d %s"
print(helloMessage % ("Kate",1,"animal"))
print(helloMessage %("Chirs", 100000, "$"))

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Kate",1,"animal"))
print(helloMessage.format("Chirs", 100000, "$"))

line = "{0:20s} costs {1:4d} €"
print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAI", 6))

line = "{0:20s} {1:4d} €"
print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAI", 6))
