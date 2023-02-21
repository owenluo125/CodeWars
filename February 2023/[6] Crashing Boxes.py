# https://www.codewars.com/kata/5a4a167ad8e1453a0b000050/python

def crashing_weights(weights):
    x = 0   # x is vertical 
    y = 0   # y is horizontal
    for z in range(len(weights[0])):
        for e in range(len(weights)-1):
            if weights[x][y] > weights[x+1][y]:
                weights[x+1][y] += weights[x][y]
                weights[x][y] = " "
            x += 1
        y += 1
        x = 0
    
    return weights[len(weights)-1]
