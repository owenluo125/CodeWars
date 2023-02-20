# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/python

def uni_total(s):
    total = 0
    for x in range(len(s)):
        total += ord(s[x])
    return total
