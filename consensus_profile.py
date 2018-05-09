#! usr/bin/env python

"""
Problem: Consensus and Profile
URL: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""

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

def matrix_profile(seqs):
	""" generate a profile matrix from a list of DNA strings. """
	length = len(min(seqs, key=len)) # in case the strings are different lengths
	matrix = [[0 for x in range(4)] for y in range(length)]
	letters = {'A':0, 'C':1, 'G':2, 'T':3}

	for i in range(length):
		for string in seqs:
			nt = string[i]
			if nt in letters:
				matrix[i][letters[nt]] += 1

	return matrix

def consensus_seq(profile):
	""" Determine the consensus sequence from a given profile matrix. """
	consensus = ''
	letter = ['A', 'C', 'G', 'T']

	for i in range(len(profile)):
		nt = profile[i].index(max(profile[i]))
		consensus += letter[nt]

	return consensus

def format_profile(profile):
	""" A generator that outputs the profile matrix in a readable format. """
	prefix = ['A', 'C', 'G', 'T']

	for i in range(4):
		line  = prefix[i] + ': '
		for j in range(len(profile)):
			line += str(profile[j][i]) + ' '

		yield line

if __name__ == '__main__':
	dataset = sys.argv[1]
	sequences = parse_fasta(dataset)
	profile = matrix_profile(sequences)
	consensus = consensus_seq(profile)

	with open('answer.txt', 'w') as outfile:
		outfile.write(consensus + '\n')
		for line in format_profile(profile):
			outfile.write(line + '\n')