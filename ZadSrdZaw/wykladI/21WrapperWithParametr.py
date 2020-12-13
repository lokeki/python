# Funkcja wrapper z parametrem

import datetime
import functools

#logFilePath = r"N:\temp\wrapper.txt"
'''
def CreateFunctionWithWrapper(func):
    def funWithWrapper(*args, **kwargs):
        file = open(logFilePath, "a")
        file.write("-" * 20 + "\n")
        file.write("Function started at {} \n".format(datetime.datetime.now().isoformat()))
        file.write("Following arguments were used: \n")
        file.write(" ". join("{}".format(x) for x in args))
        file.write("\n")
        file.write(" ".join("{} = {}".format(k,v) for (k,v) in kwargs.items()))
        file.write("\n")
        result = func(*args, **kwargs)
        file.write("Function returned {} \n".format(result))
        file.close()
        return result
    return funWithWrapper
'''
'''
def CreateFunctionWithWrapperLogToFile(logFilePath): #funkcja z nazwa pliku
    def CreateFunctionWithWrapper(func): #wraper
        def funWithWrapper(*args, **kwargs): #wszyskie funkcje
            file = open(logFilePath, "a")
            file.write("-" * 20 + "\n")
            file.write("Function started at {} \n".format(datetime.datetime.now().isoformat()))
            file.write("Following arguments were used: \n")
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{} = {}".format(k, v) for (k, v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write("Function returned {} \n".format(result))
            file.close()
            return result
        return funWithWrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapperLogToFile(r"N:\temp\wrapperChangeSalary.txt")
def ChangeSalary (empName, newSalary, isBonus = False):
    print("Changing salary for {} to {} as bonus{}".format( empName, newSalary, isBonus))
    return newSalary

@CreateFunctionWithWrapperLogToFile(r"N:\temp\wrapperChangePosition.txt")
def ChangePosition (empName, newPosition):
    print("Changing position for {} to {} ".format( empName, newPosition))
    return newPosition

#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary("Johan", 20000, True))
print(ChangeSalary("Joh", 20000, isBonus=True))
print(ChangePosition("Jorden", "Manager"))
print(ChangePosition("Mikel", "Salesman"))
'''

import os
import functools
from datetime import datetime as dt


def CreateFunctionWithWrapperLogToFile(logged_action, logFilePath):

    def CreateFunctiomWithWrapper(func):

        def FunctionWithWraper(*args, **kwargs):

            with(open(logFilePath,'a')) as file:
                file.write("Action {} executed on {} on {} \n".format(logged_action, logFilePath, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return func(*args, **kwargs)
        return FunctionWithWraper
    return CreateFunctiomWithWrapper

@CreateFunctionWithWrapperLogToFile('FILE_CREATE',r"N:\temp\wrapperLabCreate.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@CreateFunctionWithWrapperLogToFile('FILE_DELETE',r"N:\temp\wrapperLabDelete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')

'''
def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path, 'a')) as f:
                f.write('Action {} executed on {} on {}\n'.format(logged_action, path,
                                                                  dt.now().strftime("%Y-%m-%d %H:%M:%S")))

            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'N:/temp/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', r'N:/temp/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
'''