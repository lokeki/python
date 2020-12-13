#Optymalizacja funkcji przez cache# musi byc deterministyczna, miec zawsze takie
# same argumenty i taki rezultat
'''
import time
import functools

@functools.lru_cache()
def Factorial (n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))

stop = time.time()
print("Time:", stop - start)

print(Factorial.cache_info())

'''

import time
import functools


@functools.lru_cache()
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()

for i in range(1, 33):
    print(fib(i))

stop = time.time()

print(stop - start)