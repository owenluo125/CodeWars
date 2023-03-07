# https://www.codewars.com/kata/63f844fee6be1f0017816ff1/python

import math
def get_jumps(cycle_list, k):
    return math.lcm(len(cycle_list), k)/k
