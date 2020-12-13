#wrapper
#sledzenie wykonania innych funkcji
'''
import datetime
import functools

def CreateFunctionWithWrapper(func):
    def funWithWrapper(*args, **kwargs):
        print("Function started at {}".format(datetime.datetime.now().isoformat()))
        result = func(*args, **kwargs)
        print("Function returned {}".format(result))
        return result
    return funWithWrapper

@CreateFunctionWithWrapper
def ChangeSalary (empName, newSalary, isBonus = False):
    print("Changing salary for {} to {} as bonus{}".format( empName, newSalary, isBonus))
    return newSalary

#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary("Johan", 20000, True))
'''

import time
import functools

def CreateFunctionWithWraper(func):

    def functionWrapper(*args, **kwargs):

        start = time.time()
        print("Function \"{}\" started".format(func.__name__))
        result = func(*args, **kwargs)
        stop = time.time()
        timeF = stop - start
        print("Time: {}".format(timeF))
        return result

    return functionWrapper

@CreateFunctionWithWraper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

print(get_sequence(8))