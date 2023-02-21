# https://www.codewars.com/kata/57f780909f7e8e3183000078/python

def grow(arr):
    finalnum = 1
    for x in range(len(arr)):
        finalnum *= arr[x]
    return finalnum
