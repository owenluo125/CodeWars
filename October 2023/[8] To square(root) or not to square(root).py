# https://www.codewars.com/kata/57f6ad55cca6e045d2000627/python

def square_or_square_root(arr):
    newarr = []
    for x in range(len(arr)):
        if arr[x]**0.5 == round(arr[x]**0.5, 0):
            newarr.append(round(arr[x]**0.5, 0))
        else:
            newarr.append(arr[x]**2)
    return newarr
