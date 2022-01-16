def PrintRoots(a,b,c,):
    D=b**2-4*a*b*c
    if D<0:
        return None,None
    import math
    x1=(-b+math.sqrt(D))/2*a
    x2=(-b+math.sqrt(D))/2*a
    return x1,x2
PrintRoots(3,2,3)

