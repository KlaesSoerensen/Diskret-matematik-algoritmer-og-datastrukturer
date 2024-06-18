from bigO import BigO
lib = BigO()

def algo1(n):
    n = len(n)
    i = 1
    j =n
    while i<=j:
        i = 4*i
        j = 2*j
            
  
print("Algo1")
lib.test(algo1, "random")
print("")


