#! usr/bin/env python

"""
	Problem: Global Alignment with Scoring Matrix
	URL: http://rosalind.info/problems/glob/

	Given: Two protein strings s and t in FASTA format (each of length at most 
	1000 aa).
	
	Return: The maximum alignment score between s and t. Use:
        - The BLOSUM62 scoring matrix.
        - Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for 
          each gap symbol).
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

def global_align(s, t, scores, gap):
	# initialise the similarity matrix
	s_matrix = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

	# Each pos in the first row and column receives a gap penalty
	for index_s in range(1, len(s)+1):
		s_matrix[index_s][0] = index_s*gap
	for index_t in range(1, len(t)+1):
		s_matrix[0][index_t] = index_t*gap

	# Fill in the similarity matrix
	for index_s in range(1, len(s)+1):
		for index_t in range(1, len(t)+1):
			s_matrix[index_s][index_t] = max([s_matrix[index_s-1][index_t-1] + match_score(scores, s[index_s-1], t[index_t-1]),
				                              s_matrix[index_s-1][index_t] + gap,
				                              s_matrix[index_s][index_t-1] + gap])

	# The max possible score is the last cell of the similarity matrix
	return s_matrix[-1][-1]

if __name__ == '__main__':

	matrix_file = sys.argv[1]
	dataset = open(sys.argv[2]).read() # use blosum62
	s, t = parse_fasta(dataset).values()
	max_score = global_align(s, t, scoring_matrix(matrix_file), -5)
	print (max_score)