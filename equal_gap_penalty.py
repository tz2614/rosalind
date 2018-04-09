#! usr/bin/env python

"""
Problem: Global Alignment with Constant Gap Penalty
URL: http://rosalind.info/problems/gcon/

Given: Two protein strings s and t in FASTA format (each of length at most 1000
aa).

Return: The maximum alignment score between s and t. Use:
    - The BLOSUM62 scoring matrix.
    - Constant gap penalty equal to 5.

EXAMPLE INPUT:
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

EXAMPLE OUTPUT:
13
"""

import sys

def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = {}
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
            records[record_id] = ""
        else:
            records[record_id] += line
    return records

def scoring_matrix(matrix_file):
    
    ''' Read a text file of a scoring matrix and return a list of scores. The
        first element in the list is the amino acids.
    '''
    
    with open(matrix_file, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return scores

def match_score(scoring_matrix, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x+1][y])

    return cost

def global_align(s, t, matrix, gap):
	# score of best alignment ending with a match or mismatch.
	M = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
	#Initialize the gap matrices with an arbitrarily small number
	#score of best alignment ending with a space in X
	X = [[-9999 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
	#score of best alignment ending with a space in Y
	Y = [[-9999 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

	for index_s in range(1, len(s)+1):
		M[index_s][0] = gap
	for index_t in range(1, len(t)+1):
		M[0][index_t] = gap

	for index_s in range(1, len(s)+1):
		for index_t in range(1, len(t)+1):
			X[index_s][index_t] = max([M[index_s-1][index_t] + gap, 
									   X[index_s-1][index_t]])
			Y[index_s][index_t] = max([M[index_s][index_t-1] + gap,
									   Y[index_s][index_t-1]])
			M[index_s][index_t] = max([M[index_s-1][index_t-1] + match_score(matrix, s[index_s-1], t[index_t-1]),
									   X[index_s][index_t],
									   Y[index_s][index_t]])
	# The max possible score is found at the bottom-right corner of the matrix.
	return M[-1][-1]

if __name__ == '__main__':

	matrix = sys.argv[1]
	dataset = open(sys.argv[2]).read() # use Blosum62
	s, t = parse_fasta(dataset).values()
	constant_gap_score = global_align(s, t, scoring_matrix(matrix), -5)
	print (constant_gap_score)


