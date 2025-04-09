# https://www.codewars.com/kata/5a04133e32b8b998dc000089/train/python

def solve(arr):
    dominant = [arr[-1]]
    highest = arr[-1]
    for x in arr[::-1]:
        if x > highest:
            highest = x
            dominant.append(x)
    
    return list(reversed(dominant))
