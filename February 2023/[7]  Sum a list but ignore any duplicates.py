# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/python

def sum_no_duplicates(l):
    sum = 0
    for x in range(len(l)):
        if l.count(l[x]) == 1:
            sum += l[x]
    return sum
