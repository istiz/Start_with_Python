def fibonacci(n):
    if type(n) !=type(1) or n<0:
        return None
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

