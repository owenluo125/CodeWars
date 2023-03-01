# https://www.codewars.com/kata/5966e33c4e686b508700002d/python

def sum_str(a, b):
    if a.isalnum() and b.isalnum():
        return str(int(a) + int(b))
    elif a.isalnum():
        return a
    elif b.isalnum():
        return b
    else:
        return '0'
