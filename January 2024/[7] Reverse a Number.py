# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/python

def reverse_number(n):
    if n < 0:
        return int(str(n*-1)[::-1]) * -1
    else:
        return int(str(n)[::-1])
