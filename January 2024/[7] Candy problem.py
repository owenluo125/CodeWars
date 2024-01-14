# https://www.codewars.com/kata/55466644b5d240d1d70000ba/python

def candies(lst):
    result = 0
    if len(lst) > 1:
        number = max(lst)
    else:
        lst = []
        result = -1
    for x in lst:
        result += number - x
    return result
