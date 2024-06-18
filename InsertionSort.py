from time import time
import random

current_time_millis = lambda: int(round(time() * 1000))

# Perform insertion sort on givne array (following the
# Pseudocode given by Introduction to Algorithms 3rd).
# Postcondition: The given arrays is sorted in non-decreasing order.
def insertion_sort(v):
    for j in range(1, len(v)):
        key = v[j]
        # Insert v[j] into sorted sequence v[0..j-1].
        i = j - 1
        while i >= 0 and v[i] > key:
            v[i+1] = v[i]
            i = i - 1
        v[i+1] = key

#  Returns whether integers in given list are sorted in non-decreasing order.
def is_sorted(v):
    return all(v[i] <= v[i+1] for i in range(len(v)-1))

# Perform tests and output whether the implementation
# correctly sorts different inputs.
def correctness_test():
    print("Tests whether implementation correctly sorts.")
    print("----------------")
    # Initialize lists to sort.
    nonDecreasing = [1,2,3,4,5,6,7,8,9]
    nonIncreasing = [9,8,7,6,5,4,3,2,1]
    similar = [42,42,42,42,42,42]
    empty = []
    taocpNumbers = [503,87,512,61,908,170,897,275,653,426,154,509,612,677,765,703]

    # Sorts lists.
    insertion_sort(nonDecreasing)
    insertion_sort(nonIncreasing)
    insertion_sort(similar)
    insertion_sort(empty)
    insertion_sort(taocpNumbers)

    # Prints whether lists are sorted.
    print("Input (sorted non-decreasing): " + str(is_sorted(nonDecreasing)))
    print("Input (sorted non-increasing): " + str(is_sorted(nonIncreasing)))
    print("Input (similar): " + str(is_sorted(similar)))
    print("Input (empty): " + str(is_sorted(empty)))
    print("Input (TAOCP numbers): " + str(is_sorted(taocpNumbers)))
    print("----------------\n\n")

# Tests insertion sort with best case input of size n.
def best_case(n):
    # Creates list with three best case input lists.
    v = [[i for i in range(n)]]
    v.append(v[0].copy())
    v.append(v[0].copy())

    # Perform sorting three times and stores running time.
    runningTimes = []
    for i in range(3):
        t1 = current_time_millis()
        insertion_sort(v[i])
        t2 = current_time_millis()
        runningTimes.append(t2-t1)

    # Output statistics.
    print("Input size n: {}".format(n))
    avg = sum(runningTimes)/3
    print("Average running time (avg): {}".format(avg))
    print("Computes (avg/n): {}".format(avg/(n*1.0)))  # should be constant (see slides)
    print("----------------")

# Tests insertion sort with worst case input of size n.
def worst_case(n):
    # Creates list with three worst case input lists.
    v = [[i for i in reversed(range(n))]]
    v.append(v[0].copy())
    v.append(v[0].copy())

    # Perform sorting three times and stores running time.
    runningTimes = []
    for i in range(3):
        t1 = current_time_millis()
        insertion_sort(v[i])
        t2 = current_time_millis()
        runningTimes.append(t2-t1)

    # Output statistics.
    print("Input size n: {}".format(n))
    avg = sum(runningTimes)/3
    print("Average running time (avg): {}".format(avg))
    print("Computes (avg/n^2): {}".format(avg/(n*n*1.0)))  # should be constant (see slides)
    print("----------------")

# Tests insertion sort with worst case input of size n.
def random_case(n):
    # Creates list with three worst case input lists.
    v = [[random.randint(0,n-1) for i in range(n)]]
    v.append(v[0].copy())
    v.append(v[0].copy())

    # Perform sorting three times and stores running time.
    runningTimes = []
    for i in range(3):
        t1 = current_time_millis()
        insertion_sort(v[i])
        t2 = current_time_millis()
        runningTimes.append(t2-t1)

    # Output statistics.
    print("Input size n: {}".format(n))
    avg = sum(runningTimes)/3
    print("Average running time (avg): {}".format(avg))
    print("----------------")


# Perform sorting and output time measurement.
def time_implementation():
    print("Best case inputs: ")
    print("----------------")
    best_case(1_000_000)
    best_case(2_000_000)
    best_case(3_000_000)
    best_case(4_000_000)
    best_case(5_000_000)
    print()

    print("Worst case inputs: ")
    print("----------------")
    worst_case(1500)
    worst_case(2000)
    worst_case(2500)
    worst_case(3000)
    worst_case(3500)
    print()

    print("Random inputs: ")
    print("----------------")
    random_case(1500)
    random_case(2000)
    random_case(2500)
    random_case(3000)
    random_case(3500)
    print()


# Main entry point.
if __name__ == "__main__":
    correctness_test()
    time_implementation()