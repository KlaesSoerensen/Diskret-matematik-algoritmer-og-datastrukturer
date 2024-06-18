def linear_hashing_find_aux(A, x):
    possible = []
    m = len(A)
    for i in range(m):
        for j in range(m):
            position = (i + j) % m
            if A[position] == None and position == x:
                possible.append(i)
            if (A[position] == None and position != x):
                break

    return possible


if __name__ == '__main__':
    possible = linear_hashing_find_aux([22, None,55, 33, 44, None, 66], 1)
    print(possible)