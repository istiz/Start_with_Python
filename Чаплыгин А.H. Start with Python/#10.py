import math

def printRoots(a,b,c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("Korney net")


printRoots(1,2,0)




