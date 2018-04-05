#! usr/bin/env python

# creating a codon dictionary with amino acids as respective values.

"""
    http://rosalind.info/problems/mrna/

    Given: A protein string of length at most 1000 aa.

    Return: The total number of different RNA strings from which the protein
    could have been translated.
"""

import sys

codon_table = {
    'UUU': 'F',       'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F',       'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L',       'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L',       'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S',       'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S',       'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S',       'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S',       'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y',       'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y',       'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop',    'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop',    'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C',       'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C',       'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop',    'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W',       'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def codon_freq():
	freq = {}
	for keys, values in codon_table.iteritems():
		if values not in freq.keys():
			freq[values] = 0
		freq[values] += 1

	return freq

def totalRNA(protein_seq):
	freq = codon_freq()
	#print freq
	total = freq['Stop']
	#print total

	for aa in protein_seq:
		total *= freq[aa]
	return total


if __name__ == '__main__':

	protein_seq = open(sys.argv[1]).read().strip()
	print totalRNA(protein_seq) % 1000000
