# https://www.codewars.com/kata/63b9aa69114b4316d0974d2c/python

def center(graph_edges):
    return graph_edges[0][0] if graph_edges[0][0] in graph_edges[1] else graph_edges[0][1]
