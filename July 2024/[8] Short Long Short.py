# https://www.codewars.com/kata/50654ddff44f800200000007/python

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a
