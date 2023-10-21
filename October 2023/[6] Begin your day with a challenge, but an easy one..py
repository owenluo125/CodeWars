# https://www.codewars.com/kata/5873b2010565844b9100026d/python

def one_two_three(n):
    first = ""
    if n > 9:
        first += "9" * (n // 9)
    if n % 9 != 0: first += str(n % 9)
    elif n == 0: first = "0"
    second = "1" * n
    if n == 0: second = 0
    return [int(first), int(second)]
    
