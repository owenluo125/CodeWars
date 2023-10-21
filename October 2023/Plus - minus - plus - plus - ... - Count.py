# https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/python

def catch_sign_change(lst):
    if len(lst) > 0:
        prevnum = lst[0]
    changes = 0
    for x in range(len(lst)):
        if (lst[x] < 0 and prevnum >= 0) or (lst[x] >= 0 and prevnum < 0):
            changes += 1
        prevnum = lst[x]
    return changes
