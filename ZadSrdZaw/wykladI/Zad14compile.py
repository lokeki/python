'''

source = "reportLine += 1"

reportLine = 0

exec(source)

#szybciej działa compile, jak jest już skompilowany dany kod
#compile(tekst do skompilowania, plik skad został przeczytany, moud(exec, eval, simple)
sourceCompile = compile(source, 'internal variable', "exec")
exec(sourceCompile)

print(reportLine)

'''

import math
import time

def roundArgumentList():
    argumentList = []
    for i in range(1000000):
        argumentList.append(i / 10)
    return argumentList

formulasList = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argumentList = roundArgumentList()

for formula in formulasList:
    resultsList = []
    print(formula)
    start = time.time()

    for x in argumentList:
        resultsList.append(eval(formula))
    stop = time.time()
    print("Min:", min(resultsList), "Max:", max(resultsList))
    print("Time:", stop - start)

print("-" * 40)

for formula in formulasList:
    resultsList = []
    print(formula)
    start = time.time()
    formulaCompile = compile(formula, 'Internal', "eval")
    for x in argumentList:
        resultsList.append(eval(formulaCompile))
    stop = time.time()
    print("Min:", min(resultsList), "Max:", max(resultsList))
    print("Time:", stop - start)
