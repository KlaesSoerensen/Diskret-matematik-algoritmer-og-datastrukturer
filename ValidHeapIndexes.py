import itertools


def is_valid_min_heap(heap):
    """
    Checks if the given heap list is a valid min-heap.
    """
    n = len(heap)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and heap[i] > heap[left]:
            return False
        if right < n and heap[i] > heap[right]:
            return False
    return True


def is_valid_max_heap(heap):
    """
    Checks if the given heap list is a valid max-heap.
    """
    n = len(heap)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and heap[i] < heap[left]:
            return False
        if right < n and heap[i] < heap[right]:
            return False
    return True


def find_valid_positions(values, key, heap_type="min"):
    """
    Finds all the positions in a heap where the given key can be placed.
    The heap can be either a min-heap or a max-heap as specified by heap_type.
    """
    valid_positions = []
    n = len(values)
    values.remove(key)

    for perm in itertools.permutations(values):
        for i in range(n):
            heap = list(perm)
            heap.insert(i, key)
            if (heap_type == "min" and is_valid_min_heap(heap)) or (heap_type == "max" and is_valid_max_heap(heap)):
                valid_positions.append(i + 1)  # Converting 0-based to 1-based index

    return sorted(set(valid_positions))


# Modify these variables as needed
values = [1, 2, 3, 4, 5]  # Example set of values
key_to_place = 4

# Find and print the valid positions for both heap types
min_heap_positions = find_valid_positions(values.copy(), key_to_place, "min")
max_heap_positions = find_valid_positions(values.copy(), key_to_place, "max")

print("Valid positions for key", key_to_place, "in a min-heap:", min_heap_positions)
print("Valid positions for key", key_to_place, "in a max-heap:", max_heap_positions)
