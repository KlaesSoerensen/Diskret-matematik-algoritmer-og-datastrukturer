import math

# This program has not been verified to be mathematically correct.
# However, it has yet to be wrong.

class Spy:
    def __init__(self):
        self.count = 0
    
    def inc(self):
        self.count += 1

# Function to count the number of iterations
def test_algo(n, spy: Spy):
    i = n    
    j = n       # 21
    while i > 1:
        while j > i:
            j = j - 1
            spy.inc()
        i = i - 1  # O(n)

"""
    s = 0      # 20
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                for k in range(1, n):
                    s += 1
                    spy.inc()
        i = i - 1  # O(n^2)

    i = n    
    j = n       # 21
    while i > 1:
        while j > i:
            j = j - 1
            spy.inc()
        i = i - 1  # O(n)

    i = n           # 22
    while i > 1:
        j = 1
        while j < n:
            j = j + 1
            spy.inc()
        i = i / 2   # O(n log n) 
"""
from abc import ABC, abstractmethod
class ReferenceFunction(ABC):
    @abstractmethod
    def func(self, n) -> float:
        pass
    @abstractmethod
    def name(self) -> str:
        pass

class LogN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return math.log(n)
    def name(self):
        return "log(n)"

class LogNSquared(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return math.log(n)**2
    def name(self):
        return "log(n)^2"

class NSquareRoot(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n**0.5
    def name(self):
        return "sqrt(n)"
class N(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n
    def name(self):
        return "n"
class NPlusN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n + n
    def name(self):
        return "n+n"
class NLogN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n * math.log(n)
    def name(self):
        return "n*log(n)"
class LogFactorialN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return sum(math.log(i) for i in range(1, n+1))
    def name(self):
        return "log(!n)"
class NSquared(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n**2
    def name(self):
        return "n^2"
class TwoPowerN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n * math.log(2)
    def name(self):
        return "2^n"
class NPowerN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return n * math.log(n)
    def name(self):
        return "n^n"
class FactN(ReferenceFunction):
    def init(self):
        pass
    def func(self, n):
        return sum(math.log(i) for i in range(1, n+1))
    def name(self):
        return "n!"
# To Test against
complexity_functions = [LogN(), LogNSquared(), NSquareRoot(), N(), NPlusN(), NLogN(), LogFactorialN(), NSquared(), TwoPowerN(), NPowerN(), FactN()]

# Weight against smaller n values - higher n values count more 
def weightValues(values):
    return [rg * (i / len(values)) for i, rg in enumerate(values)]

def getDeltaValues(values):
    return [values[i] - values[i-1] for i in range(1, len(values))]

def lerpAgainst(values, refMin, refMax):
    return [(rg - refMin) / (refMax - refMin) for rg in values]

def lerpValues(values):
    # Linear interpolate all values into a 0-1 space
    minObservedGrowth = min(values)
    maxObservedGrowth = max(values)
    return lerpAgainst(values, minObservedGrowth, maxObservedGrowth)

def normalizeValues(values):
    # values = getDeltaValues(values)
    # values = weightValues(values)
    values = lerpValues(values)
    return values

def getNextN(index):
    return 2**index

import time
n_values = []
absoluteObservations = []
timeA = time.time()
maxTimeoutSeconds = 10
iterCounter = 1 # Some guys below got a problem with zeroes
print("Checking runtime for algorithm... " + str(maxTimeoutSeconds) + " seconds remaining.")
while True:
    current_n = getNextN(iterCounter)
    n_values.append(current_n)
    if time.time() - timeA > maxTimeoutSeconds:
        print("Algorithm checking complete, comparing to known complexities...")
        break

    spy = Spy()
    test_algo(current_n, spy)
    absoluteObservations.append(spy.count)
    iterCounter += 1

observedMin = min(absoluteObservations)
observedMax = max(absoluteObservations)
observedValuesNormalized = lerpValues(absoluteObservations)

reference_func_growth = {}
# Calculate the relative growth rates for known complexities
for compFunc in complexity_functions:
    reference_func_growth[compFunc.name()] = lerpAgainst([compFunc.func(n) for n in n_values], observedMin, observedMax)

# Find the closest match
closest_match = None
smallest_difference = float('inf')

significanceLevel = 0.01
diffs = {}
for refFuncName, refFuncGrowth in reference_func_growth.items():
    if len(refFuncGrowth) == 0:
        continue

    # Calculate the sum of absolute differences for comparison
    diffs[refFuncName] = []
    for obsVal, refFuncVal in zip(observedValuesNormalized, refFuncGrowth):
        if refFuncVal == 0:
            diffs[refFuncName].append(obsVal) 
        diffs[refFuncName].append(abs(obsVal - refFuncVal))

    diffs[refFuncName] = sum(diffs[refFuncName])

# Sort diffs on the diff value of each key in dict
sorted_keyset = sorted(diffs, key=lambda x: diffs[x])

for key in sorted_keyset:
    print(f"{key}: {diffs[key]}")

withinSignificance = []
for key in sorted_keyset:
    if diffs[key] < significanceLevel:
        withinSignificance.append(key)

if len(withinSignificance) == 0:
    withinSignificance = [sorted_keyset[0], sorted_keyset[1], sorted_keyset[2]]

print(f"\nThe closest matching growth complexity is: {', '.join(withinSignificance)}")
