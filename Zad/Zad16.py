#ternary

#wyk
#
# itRains = True
#
# if itRains:
#     print("We stay at home")
# else:
#     print("We go out")
#
# print("We stay at home" if itRains else "We go out")

musclePain = False
fever = True
weakness = False
isMan = False

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif weakness and not(musclePain and fever):
    print("Just take a rest!")
else:
    print("you may be cold")


isCheckCompleted = True
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")

