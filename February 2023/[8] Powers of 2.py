# https://www.codewars.com/kata/57a083a57cb1f31db7000028/python

def powers_of_two(n):
    new = []
    for x in range(n+1):
        new.append(2**x)
    return new
