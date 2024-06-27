def counting_sort(arr):
    if not arr:
        return arr

    print("Original array:", arr)

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Create count array and initialize all values to 0
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count_arr[num - min_val] += 1

    print("Count array:", count_arr, "-", sum(count_arr))

    # Update count array to store the cumulative count
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    print("Cumulative count array:", count_arr, "-", sum(count_arr))

    # Place the elements in the output array in sorted order
    for num in reversed(arr):
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    print("Sorted array:", output_arr, "-", sum(output_arr))

    return output_arr


# Modify the input array here
input_array = [2, 0, 6, 2, 3, 5, 5, 1, 2]

import sys
# Optional CLI input syntax: python CountingSort.py array="1 2 3 4 5 6"
for arg in sys.argv:
    if arg.startswith("array="):
        input_array = list(map(int, arg.split("=")[1].replace("\"", "").split(" ")))

sorted_array = counting_sort(input_array)