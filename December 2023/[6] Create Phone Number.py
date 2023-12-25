# https://www.codewars.com/kata/525f50e3b73515a6db000b83/python

def create_phone_number(n):
    firstPart = "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") "
    secondPart = str(n[3]) + str(n[4]) + str(n[5]) + "-"
    thirdPart = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return firstPart + secondPart + thirdPart
