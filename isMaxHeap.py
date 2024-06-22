def is_max_heap(A):
    n = len(A)

    for i in range(n // 2):
        # Check left child
        if A[2 * i + 1] > A[i]:
            return False

        # Check right child
        if 2 * i + 2 < n and A[2 * i + 2] > A[i]:
            return False

    return True

print(is_max_heap([2,1]))
print(is_max_heap([2,1,2,1]))
print(is_max_heap([2,1,2,1,2,1]))
print(is_max_heap([2,1,2,1,2,1,2,1]))
print(is_max_heap([-2,-2,-2,-2,-2,-2]))
print(is_max_heap([1,2,4,16,32,64]))
print(is_max_heap([1,-1,-1,-2,-2,-2]))