def printRoots(a,b,c):
    D = b**2-4*a*c
    import math
    print("In function D = ",D, "\nAdress:", id(D),"\n")
    x1 = (-b+math.sqrt(D))/2*a
    x2 = (-b-math.sqrt(D))/2*a
    print('x1=', x1, '\nx2=', x2)

D='test'
print('Before function call D=',D,"\nAress:",id(D),"\n")
printRoots(1.0, 0, -1.0)
print("After function call D=",D, "\nAdress",id(D),"\n")
