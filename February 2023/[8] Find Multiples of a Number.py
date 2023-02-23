# https://www.codewars.com/kata/58ca658cc0d6401f2700045f/python

def find_multiples(integer, limit):
    newint = integer
    amog = []
    while True:
        amog.append(newint)
        newint += integer
        if newint > limit:
            break
    return amog
