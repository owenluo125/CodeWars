# https://www.codewars.com/kata/644661194e259c035311ada7/python

def mul_by_n(lst, n):
    for x in range(len(lst)):
        lst[x] = lst[x] * n
    return lst
