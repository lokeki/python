def PrintAnimal(*animal):
    txt_cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
    txt_bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    txt_bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
    for animalName in animal:
        if animalName == 'cat':
            print(txt_cat)
        elif animalName == 'bear':
            print(txt_bear)
        elif animalName == 'bat':
            print(txt_bat)
        else:
            print("Cannot print", animalName, ". Correct values for the parameter are: cat, bear, bat")


PrintAnimal('cat', 'bat', 'koko', 'bear')
