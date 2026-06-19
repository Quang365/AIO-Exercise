import math

def factorial(n):
    if n < 0: 
        return
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def approx_sin(x, n):
    if n < 0:
        return
    
    sin_x = 0

    for i in range(n):
        sin_x += math.pow(-1, i) * math.pow(x, 2 * i + 1) / factorial(2 * i + 1)

    return sin_x

def approx_cos(x, n):
    if n < 0:
        return
    
    cos_x = 0

    for i in range(n):
        cos_x += math.pow(-1, i) * math.pow(x, 2 * i) / factorial(2 * i)

    return cos_x

def approx_sinh(x, n):
    if n < 0:
        return
    
    sinh_x = 0

    for i in range(n):
        sinh_x += math.pow(x, 2 * i + 1) / factorial(2 * i + 1)

    return sinh_x

def approx_cosh(x, n):
    if n < 0:
        return
    
    cosh_x = 0

    for i in range(n):
        cosh_x += math.pow(x, 2 * i) / factorial(2 * i)

    return cosh_x

print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))