# https://www.codewars.com/kata/59884371d1d8d3d9270000a5/train/python

def shake_tree(tree):
    tree = tree[:]
    for x in range(len(tree)):
        tree[x] = list(tree[x])
    
    nuts = ["" for x in range(len(tree[0]))]
    tree = [tree, [[[] for x in range(len(tree[0]))] for x in range(len(tree))]]
        
        
    for x in range(len(tree[0][0])):
        if tree[0][0][x] == "o":
            tree[1][0][x].append("o")

    for x in range(len(tree[0]) - 1):
        for y in range(len(tree[0][0])):
            if len(tree[1][x][y]) != 0:
                for z in range(len(tree[1][x][y])):
                    try:
                        if tree[0][x + 1][y] == "/":
                            tree[1][x + 1][y - 1].append("o")
                        elif tree[0][x + 1][y] == "\\":
                            tree[1][x + 1][y + 1].append("o")
                        elif tree[0][x + 1][y] == "_":
                            pass
                        else:
                            tree[1][x + 1][y].append("o")
                    except:
                        pass

    for x in range(len(tree[1][-1])):
        nuts[x] = len(tree[1][-1][x])
    
    return nuts
