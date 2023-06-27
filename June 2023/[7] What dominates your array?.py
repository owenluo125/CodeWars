# https://www.codewars.com/kata/559e10e2e162b69f750000b4/python

def dominator(arr):
    for x in arr:
        if arr.count(x) > len(arr)/2:
            return x 
    return -1
