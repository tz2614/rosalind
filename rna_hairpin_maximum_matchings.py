#! usr/bin/env python

"""
Problem: Maximum Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/mmch/

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the
bonding graph of s.
"""

from math import factorial
import sys

def parse_fasta(path, no_id=True):
    ''' Read in a Fasta file. If no_id is set to False, return a dictionary of
        sequences with associated headers; otherwise return a list of 
        sequences only.
    '''
    ids = []
    seqs = []
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))

def max_match(rna_seq):

	a, u, g, c = map(rna_seq.count, ["A", "U", "G", "C"])

	au = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
	gc = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))

	return au * gc

if __name__ == "__main__":
	dataset = sys.argv[1]
	rna_seq = parse_fasta(dataset)
	print (max_match(rna_seq))
