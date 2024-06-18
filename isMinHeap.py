def is_min_heap(arr):
    n = len(arr)

    # Check if each parent is smaller than its children
    for i in range(n // 2):
        # Check left child
        if arr[2 * i + 1] < arr[i]:
            return False

        # Check right child
        if 2 * i + 2 < n and arr[2 * i + 2] < arr[i]:
            return False

    return True


array1 = [0,1,0,1,1,0,1,1]
array2 = [0,0,0,1,1,1,0,1]
array3 = [0,0,1,0,0,1,1,0]
array4 = [0,1,0,1,0,1,0,1]
array5 = [0,0,0,0,1,1,1,1]
array6 = [1,1,1,1,0,0,0,0]
array7 = [0,0,0,0,0,0,0,0]


print(is_min_heap(array1))
print(is_min_heap(array2))
print(is_min_heap(array3))
print(is_min_heap(array4))
print(is_min_heap(array5))
print(is_min_heap(array6))
print(is_min_heap(array7))
