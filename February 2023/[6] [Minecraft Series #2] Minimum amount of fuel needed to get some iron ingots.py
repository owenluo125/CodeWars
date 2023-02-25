# https://www.codewars.com/kata/583a02740b0a9fdf5900007c/python

def calc_fuel(n):
    n *= 11
    amount = {}
    amount["lava"] = n // 800
    amount["blaze rod"] = (n - (amount["lava"] * 800)) // 120
    amount["coal"] = (n - (amount["lava"] * 800) - (amount["blaze rod"] * 120)) // 80
    amount["wood"] = (n - (amount["lava"] * 800) - (amount["blaze rod"] * 120) - (amount["coal"] * 80)) // 15
    amount["stick"] = (n - (amount["lava"] * 800) - (amount["blaze rod"] * 120) - (amount["coal"] * 80) - (amount["wood"] * 15))
    return amount
