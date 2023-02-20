# https://www.codewars.com/kata/5865918c6b569962950002a1/python

def str_count(strng, letter):
    count = 0
    for x in range(len(strng)):
        if strng[x] == letter:
            count += 1
        else:
            pass
    return count
