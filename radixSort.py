def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radixSort(arr, iterations):
    max_num = max(arr)
    exp = 1

    for _ in range(iterations):
        countingSort(arr, exp)
        exp *= 10


# Example usage:
arr = [2452, 5363, 4433, 1413, 2433, 3222, 2121]
iterations = 3

#Optional CLI Input syntax: python radixSort.py arr="[space separated list of numbers]" iterations=[number of iterations]
#Example: python radixSort.py arr="2452, 5363, 4433, 1413, 2433, 3222, 2121" iterations=3
import sys
for arg in sys.argv:
    if arg.startswith("array="):
        inputArr = arg.split("=")[1].replace("\"", "").replace(",", "").split(" ")
        inputArr = list(map(int, arr))
        arr = inputArr
    elif arg.startswith("iterations="):
        inputIter = int(arg.split("=")[1])
        iterations = inputIter

radixSort(arr, iterations)
print("Sorted array:", arr)
