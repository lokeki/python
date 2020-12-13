persons = ['Elizabeth', 'Stevena@sales.mycompany.com', 'Sebastian', 'Margaret', 'Svetlana@mycompany.eu', 'Raphael']

domain = 'mycompany.com'

emails = []

# for person in persons:
#     if '@' in person:
#         emails.append(person)
#     else:
#         email = person + '@' + domain
#         emails.append(email)

for person in persons:
    if '@' in person:
        emails.append(person)
        continue

    email = person + '@' + domain
    emails.append(email)

for email in emails:
    print(email)

#lab
menu = '''
    Choose what you want me to do for you:
    1 - COFFEE
    2 - TEA
    3 - MAKE ME SMILE
    ---------------
    To stop this script select 0
    '''

smile = '''

                              oooo$$$$$$$$$$$$oooo
                          oo$$$$$$$$$$$$$$$$$$$$$$$$o
                       oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
       o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
    oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
    "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
      $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
       "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
        $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
       o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
       $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
      o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
      $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
     """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
                "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
                  $$$o          "$$""$$$$$$""""           o$$$
                   $$$$o                                o$$$"
                    "$$$$o      o$$$$$$o"$$$$o        o$$$$
                      "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                         ""$$$$$oooo  "$$$o$$$$$$$$$"""
                            ""$$$$$$$oo $$$$$$$$$$
                                    """"$$$$$$$$$$$
                                        $$$$$$$$$$$$
                                         $$$$$$$$$$"
                                          "$$$""""
    '''
while True:
    print(menu)
    letter = int(input("Enter your choice: "))

    if letter == 0:
        break

    if letter == 1:
        print("Function COFFEE not implemented")
        input("Press ENTER")
        continue

    if letter == 2:
        print("Function Tea not implemented")
        input("Press ENTER")
        continue

    if letter == 3:
        print(smile)
        input("Press ENTER")
        continue

    input('You need to make a valid choice. Press ENTER and try again!')


