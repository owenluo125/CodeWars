# https://www.codewars.com/kata/5a8059b1fd577709860000f6/python

def alphabetic(s):
    prev = 0
    for x in range(len(s)):
        if ord(s[x]) < prev:
            return False
        prev = ord(s[x])
    return True
