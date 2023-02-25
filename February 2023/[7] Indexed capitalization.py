# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/python

def capitalize(s, ind):
    for x in range(len(ind)):
        if ind[x]-1 < len(s):
            e = s[ind[x]]
            s = s[:ind[x]] + e.upper() + s[ind[x]+1:]
    return s
