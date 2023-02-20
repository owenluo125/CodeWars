# https://www.codewars.com/kata/515e271a311df0350d00000f/python

def square_sum(numbers):
    total = 0
    for x in range(len(numbers)):
        total += numbers[x]**2
    return total
