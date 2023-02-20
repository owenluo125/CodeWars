# https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/python

def nearest_sq(n):
    x = 0
    while True:
        if x**2 >= n:
            break
        else:
            x += 1
    
    if x**2 - n > n - (x-1)**2:
        return (x-1)**2
    else:
        return x**2
