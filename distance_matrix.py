#! usr/bin/env python

"""
Problem: Creating a Distance Matrix
URL: http://rosalind.info/problems/pdst/

Given: A collection of n (n <= 10) DNA strings s,...,sn of equal length (at most
1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As
always, note that your answer is allowed an absolute error of 0.001.
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


def calc_distance(s1, s2):
	
	if len(s1) == len(s2):
		dist = float(sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1)))) / len(s1)
	else:
		print ("s1 and s2 not the same length")

	return dist

def distance_matrix(strings):
	matrix = [[0 for i in range(len(strings))] for j in range(len(strings))]	

	for x in range(len(strings)):
		for y in range(len(strings)):
			dist = float("{0:.5f}".format(calc_distance(strings[x], strings[y])))
			matrix[x][y] = dist

	return matrix

if __name__ == "__main__":
	dataset = sys.argv[1]
	strings = parse_fasta(dataset)
	matrix = distance_matrix(strings)
	with open("answer.txt",'w') as outfile:
		for line in matrix:
			outfile.write(' '.join(map(str, line)) + '\n')


