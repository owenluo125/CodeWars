# https://www.codewars.com/kata/5287e858c6b5a9678200083c/python

def narcissistic( value ):
    amount = len(str(value))
    number = 0
    for x in range(amount):
        number += int(str(value)[x])**amount
    return value == number
