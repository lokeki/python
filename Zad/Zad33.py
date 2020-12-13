#timedelta/date/datetime

import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata), len(factortable))

if len(inputdata) == len(factortable):
    print("OK")
    for i in range(len(inputdata)):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print("Value:",minvalue, maxvalue)
        minIntiget = math.floor(minvalue)
        maxIntiger = math.ceil(maxvalue)
        print("Intiger:",minIntiget, inputdata[i], maxIntiger)
else:
    print("inputdata and factortable need to have equal number of elements")

import random


for i in range(len(inputdata)):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print("Value:",minvalue, maxvalue)
    minIntiget = math.floor(minvalue)
    maxIntiger = math.ceil(maxvalue)
    print("Intiger:",minIntiget, inputdata[i], maxIntiger)

import datetime

print(datetime.datetime.today())
print("today", datetime.datetime.now().strftime("%Y-%m-%d"))
