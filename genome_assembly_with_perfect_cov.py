#! usr/bin/env python

"""
Problem: Genome Assembly with Perfect Coverage
URL: http://rosalind.info/problems/pcov/

Given: A collection of (error-free) DNA kk-mers (k<=50) taken from the same 
strand of a circular chromosome. In this dataset, all kk-mers from this strand 
of the chromosome are present, and their de Bruijn graph consists of exactly 
one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus 
corresponding to a candidate cyclic chromosome).
"""

import sys

def get_superstring(collection):
    db = dict([(dna[:-1], dna[1:]) for dna in collection])
    k = db.iterkeys().next()
    superstring = ''
    
    while len(superstring) < len(collection):
        superstring += db[k][-1]
        k = db[k]
        
    return superstring

if __name__ == '__main__':

	dataset = sys.argv[1]
	with open(dataset) as data_file:
		collection = data_file.read().rstrip().replace('\r', '').split('\n')
    
    	print get_superstring(collection)