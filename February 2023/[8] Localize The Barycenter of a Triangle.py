# https://www.codewars.com/kata/5601c5f6ba804403c7000004/python

def bar_triang(a, b, c):
    coor = []
    coor.append(round((a[0]+b[0]+c[0])/3,4))
    coor.append(round((a[1]+b[1]+c[1])/3,4))
    return coor
