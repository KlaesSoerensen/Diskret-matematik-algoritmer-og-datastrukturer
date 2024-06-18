""" print(any(a**2 + 1 == 82 for a in range(-1000, 1000+1)))
print(all(a < a**2 for a in range(-1000, 1000+1)))
print(any(any(a == b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1)))
print(all(any(2*a > b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1)))
print(all(any(a == 2 * b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1)))
print(all(any(a == b + 2 for b in range(-2000, 2000+1)) for a in range(-1000, 1000+1)))
print(all(all(a < b or a > b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1)))
print(not any(all(a**2 == b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1)) == any(all(a**2 != b for b in range(-1000, 10000+1)) for a in range(-100, 100+1)))
print(any(all(a**2 != b for b in range(-1000, 1000+1)) for a in range(-1000, 1000+1))) """
""" 
print(all(x**2 > 2*x for x in range(-1000,1000+1)))
print(all(x**2<2*x for x in range(-1000,1000+1)))
print(all((x<5 or x**2>2*x) for x in range(-1000,1000+1)) )
print(all(any(x + y ==2*x for y in range(-2000, 2000+1)) for x in range(-1000, 1000+1)))
print(not any(all(x+y ==2*x for y in range(-1000, 1000+1)) for x in range(-1000, 1000+1)))
print(all(all(x+y == 2*x for y in range(-1000, 1000+1)) for x in range(-1000, 1000+1)))
print(not any(any(x+y == 2*x for y in range(-1000, 1000+1)) for x in range(-1000, 1000+1)) == all(any(x+y!=2*x for y in range(-1000, 1000+1))for x in range(-1000, 1000+1))) """

""" for n in range(1,100):
    if ((1/2)**(n-1)-(1/2)**n) == ((1/2)**(0)-(1/2)**1):
        print(True)
    else:
        print(False) """

for n in range(1,10):
    if ((1/2)**(n-1)-(1/2)**n)== (1-1/2):
        print(True)
    else:
        print(False)
