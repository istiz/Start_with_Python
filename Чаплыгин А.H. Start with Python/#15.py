a = (input("a = "))
b = (input("b = "))
c = (input("c = "))
def PrintRoots(a, b, c):

    D = b**2-4*a*c
    import math
    x1 = (-b+math.sqrt(D))/2*a
    x2 = (-b-math.sqrt(D))/2*a

print (x1,x2)

