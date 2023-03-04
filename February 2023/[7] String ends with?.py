# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/python

def solution(text, ending):
    return True if text[-len(ending):] == ending else False
