# https://www.codewars.com/kata/5951d30ce99cf2467e000013/python

def pythagorean_triple(integers):
    integers.sort()
    return True if integers[1] + integers[2] == integers[0]**2 else False
