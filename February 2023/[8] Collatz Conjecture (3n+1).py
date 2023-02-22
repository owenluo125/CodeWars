# https://www.codewars.com/kata/577a6e90d48e51c55e000217/python

def hotpo(n):
    count = 0
    while True:
        if n == 1:
            return count
        elif n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        count += 1
