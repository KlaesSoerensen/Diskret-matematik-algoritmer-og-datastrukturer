import math

class Spy:
    def __init__(self):
        self.count = 0
    
    def inc(self):
        self.count += 1

# Function to count the number of iterations
def test_algo(n, spy: Spy):
    i = 1
    j = n
    while i <= j:
        i = 4 * i
        j = 2 * j
        k = 0
        while k < n: 
            k = k + 1
            spy.inc()

# Known growth complexities using logarithms to prevent overflow
def log_n(n):
    return math.log(n) if n > 0 else float('inf')

def log_n_squared(n):
    return (math.log(n) if n > 0 else float('inf'))**2

def n_twelve(n):
    return n**(1/2)

def n(n):
    return n

def n_plus_n(n):
    return n + n

def n_log_n(n):
    return n * (math.log(n) if n > 0 else float('inf'))

def log_factorial_n(n):
    return sum(math.log(i) for i in range(1, n+1)) if n > 1 else float('inf')

def n_squared(n):
    return n**2

def two_power_n(n):
    return n * math.log(2)

def n_power_n(n):
    return n * math.log(n)

def factorial_n(n):
    return sum(math.log(i) for i in range(1, n+1))

def getNArray(count):
    return [2 ** i for i in range(1, count)]

# Generate the data
n_values = getNArray(20)
spies = [Spy() for _ in n_values] # Object pooling
iteration_counts = []
for i in range(len(n_values)):
    test_algo(n_values[i], spies[i])
    iteration_counts.append(spies[i].count)


# Handle potential zero values in iteration counts
relative_growth = []
for i in range(len(iteration_counts)):
    if i > 0 and iteration_counts[i-1] != 0:
        relative_growth.append(iteration_counts[i] / iteration_counts[i-1])
    else:
        relative_growth.append(1)

# Calculate the relative growth rates for known complexities
complexity_functions = [log_n, log_n_squared, n_twelve, n, n_plus_n, n_log_n, log_factorial_n, n_squared, two_power_n, n_power_n, factorial_n]
complexity_names = ["log(n)", "log(n)^2", "n^1/2", "n", "n+n", "n*log(n)", "log(!n)", "n^2", "2^n", "n^n", "!n"]
complexity_growth = {name: [] for name in complexity_names}

for func, name in zip(complexity_functions, complexity_names):
    values = [func(n) for n in n_values]
    growth = []
    # TODO: Detect and handle constant offset in tested algorithm
    for i in range(len(values)):
        if i > 0 and values[i-1] != 0:
            growth.append(values[i] / values[i-1])
        else:
            growth.append(1)
    # Using logs to prevent overflow and domain errors
    growth_log = [math.log(g) if g > 0 else float('inf') for g in growth]
    complexity_growth[name] = growth_log

# Find the closest match
closest_match = None
smallest_difference = float('inf')

print("Relative Growth of the Given Function:")
# print(relative_growth)
print("\nRelative Growth of Known Complexities:")

# Convert relative growth of the given function to logs to match the comparison method
relative_growth_log = [math.log(rg) if rg > 0 else float('inf') for rg in relative_growth]

for name, growth in complexity_growth.items():
    # print(f"{name}: {growth}")
    # Calculate the sum of absolute differences for comparison
    difference = sum(abs(rg - cg) for rg, cg in zip(relative_growth_log, growth))
    if difference < smallest_difference:
        smallest_difference = difference
        closest_match = name

print(f"\nThe closest matching growth complexity is: {closest_match}")
