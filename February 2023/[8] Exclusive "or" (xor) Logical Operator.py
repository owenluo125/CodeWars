# https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c/python

def xor(a,b):
    test = 0
    if a == True:
        test += 1

    if b == True:
        test += 1
    
    if test == 2 or test == 0:
        return False
    else:
        return True
