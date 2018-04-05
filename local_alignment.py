#! usr/bin/env python

"""
Problem: Local Alignment with Scoring Matrix
URL: http://rosalind.info/problems/loca/

Given: Two protein strings s and t in FASTA format (each having length at most
1000 aa).

Return: A maximum alignment score along with substrings r and u of s and t,
respectively, which produce this maximum alignment score (multiple solutions may
exist, in which case you may output any one). Use:
    - The PAM250 scoring matrix.
    - Linear gap penalty equal to 5.

EXAMPLE INPUT:
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

EXAMPLE OUTPUT:
(note: this is correct, but different than Rosalind sample output):
23
MEANLYPRTEINSTRIN
LEASANTLYEINSTEIN

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

def match_score(scoring_matrix, a, b):
    ''' Return the score from the scoring matrix. '''
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x+1][y])

    return cost

def scoring_matrix(matrix_file):
    ''' Read a text file of a scoring matrix and return a list of scores. The
        first element in the list is the amino acids.
    '''
    with open(matrix_file, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return scores

def alignment_score(s, t, scores, gap):
	'''Returns two matrices of the edit distance and edit alignment between string s and t.'''

	# Initialise the similarity and traceback matrices.
	s_matrix = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
	traceback = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

	best_score = 0
	best_pos = (0, 0)

	# Fill in the matrices.

	for index_s in range(1, len(s)+1):
		for index_t in range(1, len(t)+1):
			cost = [s_matrix[index_s-1][index_t-1] + match_score(scores, s[index_s-1], t[index_t-1]),
			        s_matrix[index_s-1][index_t] + gap,
			        s_matrix[index_s][index_t-1] + gap]
			s_matrix[index_s][index_t] = max(cost)
			traceback[index_s][index_t] = cost.index(s_matrix[index_s][index_t])

			if s_matrix[index_s][index_t] >= best_score:
				best_score = s_matrix[index_s][index_t]
				best_pos = [index_s, index_t]

	# initialise i, j as the index of the highest score.

	i, j = best_pos

	# initialise the aligned strings as prefix of the best position.

	r, u = s[:i], t[:j]

	# trace back to the edge of the matrix starting at the best position.

	while traceback[i][j] != 3 and i*j != 0:
		if traceback[i][j] == 0: # a match
			i -= 1
			j -= 1
		elif traceback[i][j] == 1: # an insertion
			i -= 1
		elif traceback[i][j] == 2: # a deletion
			j -= 1

	# The optimal alignment is then the suffix of the end of the traceback

	r = r[i:]
	u = u[j:]

	return str(best_score), r, u

if __name__ == '__main__':

	matrix_file = sys.argv[1]
	dataset = open(sys.argv[2]).read()
	s, t = parse_fasta(dataset).values()
	alignment =  alignment_score(s, t, scoring_matrix(matrix_file), -5)
	print ('\n'.join(alignment))
