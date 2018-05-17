#! usr/bin/env python

"""
Problem: Genome Assembly Using Reads
URL: http://rosalind.info/problems/gasm/

Given: A collection S of (error-free) reads of equal length (not exceeding 
50 bp). In this dataset, for some positive integer k, the de Bruijn graph 
BkBk on Sk+1 U Srck+1 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its 
reverse complement.
"""

from itertools import chain
import sys

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

def complement(Nucleotide):
    if Nucleotide == "A":
        return "T"
    elif Nucleotide == "T":
        return "A"
    elif Nucleotide == "C":
        return "G"
    elif Nucleotide == "G":
        return "C"
    else:
        return ""       

def ReverseComplement(Pattern):
    revComp = [] # output variable
    for x in Pattern:
        revComp.append(x)
    revComp = reverse(revComp)
    revComp = [complement(x) for x in revComp]
    return "".join(revComp)

def cyclic_superstring(dna):
	flatten = lambda listOflists: chain.from_iterable(listOflists)

	n = len(dna)
	length = len(dna[0]) # assumes all strings are the same length

	for k in range(length-1, 1, -1):
		adj = dict(flatten([[(d[i:i+k], d[i+1:i+k+1]) for i in range(length-k)] for d in dna]))
		first = kmer = next(iter(adj))
		superstring = ''

		while True:
			if kmer in adj:
				superstring += kmer[-1]
				kmer = adj.pop(kmer)
				if kmer == first:
					return superstring
			else:
				break

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		dna = data_file.read().strip().split('\n')
		dna = list(set(dna + [ReverseComplement(i) for i in dna])) # Add the reversecomplement of each string.

	print cyclic_superstring(dna)


