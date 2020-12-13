import datetime
import os

dataInputCatalog = r'c:\temp\data_input'
dataOutputCatalog = r'c:\temp\data_output'
today = datetime.date.today()
todayOutputCatalog = os.path.join(dataOutputCatalog, today.strftime("%Y-%m-%d"))

isInputCatalog =  os.path.isdir(dataInputCatalog)

isOutputCatalog = os.path.isdir(dataOutputCatalog)

isTodayOutputCatalog = not(os.path.isdir(todayOutputCatalog)) and not(os.path.isfile(todayOutputCatalog))

if isInputCatalog and isOutputCatalog and not isTodayOutputCatalog:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')

    # display detailed error conditions
    if not isInputCatalog:
        print("Input catalog %s must exist!" % dataInputCatalog)
    if not isOutputCatalog:
        print("Output catalog %s must exist!" % dataOutputCatalog)
    if not isTodayOutputCatalog:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % todayOutputCatalog)





