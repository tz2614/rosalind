#! usr/bin/env python

"""
Problem: Global Alignment with Scoring Matrix and Affine Gap Penalty
URL: http://rosalind.info/problems/gaff/

Given: Two protein strings s and t in FASTA format (each of length at most 100
aa).

Return: The maximum alignment score between s and t, followed by two augmented
strings s' and t' representing an optimal alignment of s and t. Use:
    - The BLOSUM62 scoring matrix.
    - Gap opening penalty equal to 11.
    - Gap extension penalty equal to 1.


EXAMPLE INPUT:
>Rosalind_49
PRTEINS
>Rosalind_47
PRTWPSEIN

EXAMPLE OUTPUT:
8
PRT---EINS
PRTWPSEIN-
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

def global_align_with_affine(s, t, scores, gap, gap_e):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''
    # Initialize the three score matrices...
    M = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)] # a (mis)match
    X = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)] # a gap in X
    Y = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)] # a gap in Y

    # ...and the traceback matrices.
    traceM = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
    traceX = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
    traceY = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

    # Initialize the edges of the X and Y matrices with an arbitrarily
    # large number (closer to negative infinity, the better) so it doesn't
    # affect calculations.
    for index_s in range(1, len(s)+1):
        M[index_s][0] = gap + gap_e*(index_s-1)
        X[index_s][0] = -9999
        Y[index_s][0] = -9999
    for index_t in range(1, len(t)+1):
        M[0][index_t] = gap + gap_e*(index_t-1)
        X[0][index_t] = -9999
        Y[0][index_t] = -9999

    # Fill in the matrices.
    for index_s in range(1, len(s)+1):
        for index_t in range(1, len(t)+1):
            costX = [M[index_s-1][index_t] + gap,
                     X[index_s-1][index_t] + gap_e]
            X[index_s][index_t] = max(costX)
            traceX[index_s][index_t] = costX.index(X[index_s][index_t])
            
            costY = [M[index_s][index_t-1] + gap,
                     Y[index_s][index_t-1] + gap_e]
            Y[index_s][index_t] = max(costY)
            traceY[index_s][index_t] = costY.index(Y[index_s][index_t])

            costM = [M[index_s-1][index_t-1] + match_score(scores, s[index_s-1], t[index_t-1]),
                     X[index_s][index_t],
                     Y[index_s][index_t]]
            M[index_s][index_t] = max(costM)
            traceM[index_s][index_t] = costM.index(M[index_s][index_t])
            
    # The max possible score is found at the bottom-right of the match matrix
    max_score = M[-1][-1]

    # Initialize the aligned strings as the input strings.
    s_align, t_align = s, t

    # Get the traceback starting position, i.e. the greatest value.
    scores = [X[index_s][index_t], Y[index_s][index_t], M[index_s][index_t]]
    max_score = max(scores)
    traceback = scores.index(max_score)

    # Initialize the values of i,index_t
    index_s, index_t = len(s), len(t)

    # Traceback to build alignment.
    while index_s>0 and index_t>0:
        if traceback == 0:
            if traceX[index_s][index_t] == 0:
                traceback = 2
            index_s -= 1
            t_align = t_align[:index_t] + '-' + t_align[index_t:]

        elif traceback == 1:
            if traceY[index_s][index_t] == 0:
                traceback = 2
            index_t -= 1
            s_align = s_align[:index_s] + '-' + s_align[index_s:]

        elif traceback == 2:
            if traceM[index_s][index_t] == 1:
                traceback = 0
            elif traceM[index_s][index_t] == 2:
                traceback = 1
            else:
                index_s -= 1
                index_t -= 1

    # Fill in any leading gaps.
    for remaining in range(index_s):
        t_align = t_align[:0] + '-' + t_align[0:]
    for remaining in range(index_t):
        s_align = s_align[:0] + '-' + s_align[0:]

    return str(max_score), s_align, t_align

if __name__ == '__main__':

	matrix = sys.argv[1]
	dataset = open(sys.argv[2]).read() # use Blosum62
	s, t = parse_fasta(dataset).values()
	alignment = global_align_with_affine(s, t, scoring_matrix(matrix), -11, -1)
	alignment = '\n'.join(alignment)
	print alignment
