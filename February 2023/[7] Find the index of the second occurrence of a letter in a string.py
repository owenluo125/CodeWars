# https://www.codewars.com/kata/63f96036b15a210058300ca9/python

def second_symbol(s, symbol):
    count = 0
    for x in range(len(s)):
        if s[x] == symbol:
            count += 1
            if count == 2:
                return x
    return -1
