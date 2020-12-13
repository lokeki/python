# Zwaracanie funkcji
#
# def Calculate ( kind = "+", *args):
#     result = 0
#
#     if kind == "+":
#
#         for a in args:
#             result += a
#
#     elif kind == '-':
#
#         for a in args:
#             result -= a
#
#     return result
#
# def CreateFunction(kind = "+"):
#     source = '''
# def f(*args):
#     result = 0
#     for a in args:
#         result {}= a
#     return result
#     '''.format(kind)
#     exec(source, globals())
#
#     return f
#
# fAdd = CreateFunction("+")
# print(fAdd(1,2,3,4))
# fSubs = CreateFunction("-")
# print(fSubs(1,2,3,4))

import datetime
def TimeFunk(timeF = 'm' ):
    if timeF == 'm':
        sec = 60
    elif timeF == 'h':
        sec = 3600
    elif timeF == 'd':
        sec = 86400
    source = '''
def f(start, end):
    temp = end - start
    tempSec = temp.total_seconds()
    return divmod(tempSec, {})[0]
    '''.format(sec)
    exec(source, globals())
    return f

TimeFunk()

f_minutes = TimeFunk('m')
f_hours = TimeFunk('h')
f_days = TimeFunk('d')

start = datetime.datetime(2019, 12, 10, 0, 0, 0)
end = datetime.datetime(2020, 12, 10, 0, 0, 0)

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))