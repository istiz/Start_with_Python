

def PrintRoots(a, b, c):
    a = input('Coeff A?:')
    print('A', a)
    b = input('Coeff B?')
    print('B', b)
    c = input('Coeff C?')
    print('C', c)
    D = b**2-4*a*c
    import math
    x1 = (-b+math.sqrt(D))/2*a
    x2 = (-b-math.sqrt(D))/2*a
    return x1, x2




