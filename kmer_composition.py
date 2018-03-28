#! usr/bin/env python

"""

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.


>>> dna = '''CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
... CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
... TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
... AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
... GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
... CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
... CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'''

>>> problem(dna, 4)
4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1

"""

from collections import Counter
from itertools import product
import sys

# list all kmers in the dna string s of length k.

def kmers(s, k):
	return [s[i:i+k] for i in range(len(s)-k+1)]

# return the number of kmers within the dna string s.

def kmer_composition(s, k):
	# creates a dictionary of kmers with corresponding values representing the number of times it is seen in the dna string s.

	c = Counter(kmers(s, k))
	return [c[''.join(kmer)] for kmer in product('ACGT', repeat=k)]

def problem(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = ""
    record_id = None
    for line in [lines.strip() for lines in dataset.splitlines()]:
        
        if line.startswith('>'):
            records_id = line[1:]
        else:
            records += line
            #print records
    
    return kmer_composition(records, 4)

if __name__ == '__main__':

    dataset = open(sys.argv[1]).read()
    print ' '.join(map(str, problem(dataset)))


