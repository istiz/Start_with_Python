def f1():
    print("f1() begins")
    a=1/0
    print("f1() ends")

def f2():
    print("f2() begins")
    f1()
    print("f2() ends")

def f3():
    print("f3() begins")
    f2()
    print("f3() ends")

print("Main program begins")
f3()
print("Main program ends")
