# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/python

def descending_order(num):
    digits = list(str(num))
    digits.sort(reverse=True)
    return int(''.join(digits))
