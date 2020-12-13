#wyk/ for

persons = ['Elizabeth', 'Stevena', 'Sebastian', 'Margaret', 'Svetlana', 'Raphael']
domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print(person, '\temail:\t', email)
print()
#lab

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dataList in data:
    print("-------------------------------")
    print(dataList.upper())
    elements = dataList.split(":")
    print("-------------------------------")
    #print(elements)
    #print()
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])
