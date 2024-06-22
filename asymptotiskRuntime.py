import bigO
lib = bigO()

def algo1(n):
    i = n
    s = 0
    while i >= 1:
        for j in range(i, i * 2):
            s = s + 1
        i = math.floor(i / 2)
            
  
print("Algo1")
lib.test(algo1, "random")
print("")


