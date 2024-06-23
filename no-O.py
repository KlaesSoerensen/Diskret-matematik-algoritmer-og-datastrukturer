def algo(n, captureGroup):
    i = 1
    while i <= n:
        j = n
        while j > i:
            captureGroup[0] += 1
            j = j - 1
        i = 2 * i

inputs = [0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
captureGroup = [0]

for n in inputs:
    algo(n, captureGroup)
    print(captureGroup[0], " for n: ", n)
    captureGroup[0] = 0