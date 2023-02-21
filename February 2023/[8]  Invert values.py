# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/python

def invert(lst):
    newlst = []
    for x in range(len(lst)):
        newlst.append(lst[x] * -1)
    return newlst
