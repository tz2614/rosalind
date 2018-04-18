#! usr/bin/env python

"""
Problem: Perfect Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/pmch/

Given: An RNA string s of length at most 80 bp having the same number of
occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the
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

if __name__ == '__main__':

	dataset = sys.argv[1]
	rna_seq = parse_fasta(dataset)
	perfect_matching = factorial(rna_seq.count('A')) * factorial(rna_seq.count('C'))
	print (perfect_matching)

