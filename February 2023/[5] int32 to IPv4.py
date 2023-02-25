# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/python

def int32_to_ip(int32):
    first = int32 // (256**3)
    second = (int32 - (first * (256**3))) // (256**2)
    third = (int32 - (first * (256**3)) - (second * (256**2))) // (256)
    fourth = (int32 - (first * (256**3)) - (second * (256**2)) - (third * 256)) % 256
    return str(first) + "." + str(second) + "." + str(third) + "." + str(fourth)
