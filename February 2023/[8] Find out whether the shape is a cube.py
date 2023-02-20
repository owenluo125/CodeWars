# https://www.codewars.com/kata/58d248c7012397a81800005c/python

def cube_checker(volume, side):
    if side**3 == abs(volume) and volume > 0:
        return True
    else:
        return False
