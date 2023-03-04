# https://www.codewars.com/kata/563fb342f47611dae800003c/python

def trim(phrase, size):
    return phrase if len(phrase) <= size else phrase[:size] + "..." if size <= 3 else phrase[:size-3] + "..."
