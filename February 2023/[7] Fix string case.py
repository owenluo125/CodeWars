# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/python

def solve(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper = 0
    lower = 0
    for x in range(len(alphabet)):
        lower += s.count(alphabet[x])
        upper += s.count(alphabet[x].upper())
    
    if upper > lower:
        return s.upper()
    else:
        return s.lower()
