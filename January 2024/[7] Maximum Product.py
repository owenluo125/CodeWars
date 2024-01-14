# https://www.codewars.com/kata/5a4138acf28b82aa43000117/python

def adjacent_element_product(array):
    max = array[0] * array[1]
    for x in range(len(array)-1):
        if array[x] * array[x+1] > max:
            max = array[x] * array[x+1]
    return max
            
