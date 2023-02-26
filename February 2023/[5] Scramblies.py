# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python

def scramble(s1, s2):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(alpha)):
        if s1.count(alpha[x]) < s2.count(alpha[x]):
            return False
    return True
