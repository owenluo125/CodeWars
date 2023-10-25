# https://www.codewars.com/kata/56b97b776ffcea598a0006f2/python

def bubblesort_once(l):
    m = []
    if len(l) > 0:
        m = [l[0]] 
    for x in range(1, len(l)):
        m.append(l[x])
        if m[x] < m[x-1]:
            m[x], m[x-1] = m[x-1], m[x]
    return m
            
