# zmienne/ funkcje id()/ is

#wszystkie zmienne mają jedno miejsce w pamięci, po zmianie jednej zmienia się id
a = b = c = 10

print("a: ", a, "a id:",  id(a), "b: ", b, "b id:",  id(b), "c: ", c, "c id:",  id(c))

a = 20

print("a: ", a, "a id:",  id(a), "b: ", b, "b id:",  id(b), "c: ", c, "c id:",  id(c))

a = b = c = [1,2,3]

a.append(4)

print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))

x = 10
y = 10
print("x:", id(x), "y:", id(y))

y = y + 1 - 1
print("x:", id(x), "y:", id(y))

y = y + 1234567890 - 1234567890
print("x:", id(x), "y:", id(y))