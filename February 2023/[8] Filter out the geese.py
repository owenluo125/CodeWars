# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/python

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    newbirds = []
    for x in range(len(birds)):
        if birds[x] not in geese:
            newbirds.append(birds[x])

    return newbirds
