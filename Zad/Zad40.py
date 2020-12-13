import os
import  time

print(os.getcwd())

dir = input('enter directory name: ')
if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
    file = input("enter file name:")
    path = os.path.join(dir,file)

    if os.path.isfile(path):
        print("This path do not exists")
    else:
        print(time.localtime(os.path.getatime(path)))
        print(os.path.getsize(path))
        print(os.getcwd())
        print(os.path.abspath(path))
