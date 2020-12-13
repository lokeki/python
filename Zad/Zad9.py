message = 'Document "cv.doc" was printed on printer: XEROX'

print(message[message.find('"') + 1 : message.find('"', message.find('"')+1)])

q = "THE EYES"
print(q[:7])

q = 'a gentelman'
print(q[3:])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2 :]
print(time)

tmp = line[line.find('"') + 1 : ]
title = tmp[: tmp.find('"')]
print(title)

line1 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'

print(line1[line1.find(':') + 2 :])
print(line1[line1.find('"') + 1 : line1.find('"', line1.find('"') + 1)])

