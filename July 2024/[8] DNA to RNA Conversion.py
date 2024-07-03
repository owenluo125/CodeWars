# https://www.codewars.com/kata/5556282156230d0e5e000089/python

def dna_to_rna(dna):
    for x in range(len(dna)):
        if dna[x] == "T":
            dna = dna[:x] + "U" + dna[x+1:]
    return dna
