import math

print("ax^2+bx+c=0:")

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

discr = b**2 - 4 * a * c
print(discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Korney net")
