# https://www.codewars.com/kata/57202aefe8d6c514300001fd/python

def sale_hotdogs(n):
    return 100 * n if n<5 else 95*n if n<10 else n * 90
