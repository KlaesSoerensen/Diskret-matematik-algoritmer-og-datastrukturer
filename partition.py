def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 # index of smaller element
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place the pivot element at its correct position
    return i + 1  # return the index of the pivot element

# Test the function
#Remember to add a 0 first since the array can be excluding the zero index
arr = [6,2,4,5,1,7,3]
high = len(arr) - 1
low = 0
pivot_index = partition(arr, low, high)
print(f"Array after partitioning: {arr}")
print(f"Pivot index: {pivot_index}")
