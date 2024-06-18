def transitiveClosure(matrix):
    result = ""
    length = len(matrix)
    for k in range(0, length):
        for row in range(0, length):
            for col in range(0, length):
                matrix[row][col] = matrix[row][col] or (matrix[row][k] and matrix[k][col])
        result += ("\n W" + str(k) + " is: \n" + str(matrix).replace("],", "] \n") + "\n")
    result += ("\n Transitive closure is \n" + str(matrix).replace("],", "]\n"))
    # print(result)
    return matrix

def toMatrix(R, n):
    A = []

    for i in range(0, n):
        A.append([])
        for j in range(0, n):
            data = 0
            if (i, j) in R:
                data = 1
            A[i].append(data)

    return A

def fromMatrix(A, n):
    B = []
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] == 1:
                B.append((i, j))

    return B

def toNumbers(R, nodes):
    A = []
    for r in R:
        a = (nodes.index(r[0]), nodes.index(r[1]))
        A.append(a)

    return A

def toChar(R, nodes):
    A = []
    for r in R:
        a = (nodes[r[0]], nodes[r[1]])
        A.append(a)

    return A

def getDifference(A, B, n):
    C = []
    for i in range(0, n):
        for j in range(0, n):
            if A[i][j] != B[i][j]:
                C.append((i, j))

    return C


nodes = ['a', 'b', 'c']
relations = [
    ('a','b'),('b','a'), ('b','b'), ('b','c')
]

print("Relationer:")
print(relations)
numRelations = toNumbers(relations, nodes)
print("Relationer som tal:")
print(numRelations)
print()

# Data strukturs oversættelse og luknings beregninger
n = len(nodes)

print("Rå luknings output")
# Til matrix
matrixRelations = toMatrix(numRelations, n)
print(matrixRelations)

# Lav lukning
transitiveMatrixRelations = transitiveClosure(matrixRelations)
print(transitiveMatrixRelations)

transitiveNumRelations = fromMatrix(transitiveMatrixRelations, n)

print()
print("Resultat efter lukninger er tilføjet:")
transitiveRelations = toChar(transitiveNumRelations, nodes)
print(transitiveRelations)

print()
print("Lukninger genereret")
transitiveNumRelationsAdded = getDifference(toMatrix(numRelations, n), transitiveMatrixRelations, n)
transitiveRelationsAdded = toChar(transitiveNumRelationsAdded, nodes)
print(transitiveRelationsAdded)
