#!/usr/bin/env python   

"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

>>> problem('ACGTACGTGACG', 'GTA')
3 4 5
"""


import sys

def findmotif(dataset):
    with open (dataset) as fasta_filehandle: 

        DNA = ""
        motif = ""
        # count keeps track of the number of DNA strings
        count = 0    
    
        for line in fasta_filehandle:
            line = line.strip()
            
            if line.startswith(">"):
                count += 1  
            # create the DNA string
            elif count == 1:
                DNA += line
            # create the intron string
            elif count > 1:
                motif += line

        positions = []
        DNA = list(DNA)
        #print DNA
        motif = list(motif)
        #print motif
        basecount = 0

        for motifbase in motif:

            i = DNA.index(motifbase) + 1
            basecount += i
            positions.append(basecount)
            DNA = DNA[i:]

        return positions
  
dataset = sys.argv[1]
print ' '.join(map(str, findmotif(dataset)))