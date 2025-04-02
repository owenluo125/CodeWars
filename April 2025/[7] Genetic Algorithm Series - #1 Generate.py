# https://www.codewars.com/kata/567d609f1c16d7369c000008/train/python

def generate(length):
    import random
    binary = []
    for x in range(0,length):
        binary.append(str(random.randint(0,1)))
    
    return binary
