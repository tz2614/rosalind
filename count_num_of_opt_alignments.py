#! usr/bin/env python

'''
Problem: Counting Optimal Alignments
URL: http://rosalind.info/problems/ctea/

Given: Two protein strings s and t in FASTA format, each of length at most 1000
aa.

Return: The total number of optimal alignments of s and t with respect to edit
alignment score, modulo 134,217,727 (227-1).
'''

import sys

def parse_fasta(dataset):

    """
    Parses data in FASTA format, returning a dictionary of ID's and values
    """

    records = {}
    record_id = None

    for line in [lines.strip() for lines in dataset.splitlines()]:
        
        if line.startswith('>'):
            records_id = line[1:]
            records[records_id] = ""
        else:
            records[records_id] += line
            #print records
    
    return records


def count_alignments(s, t):
	"""
	calculate the minimum edit distance first between the two strings s and t,
	then the number of alignments with that score modulo 2^27 -1
	"""

	# initialise distance and alignment count matrices with zeros
	distance = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]
	counts = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

	# each pos in the first row and column of the distance matrix receives a -1 gap penalty
	# similarly, each pos of the counts matrix starts as 1

	for index_s in range(0, len(s)+1):
		distance[index_s][0] = index_s
		counts[index_s][0] = 1

	for index_t in range(1, len(t)+1):
		distance[0][index_t] = index_t
		counts[0][index_t] = 1

	# Fill in the matrices.
	for index_s in range(1, len(s)+1):
		for index_t in range(1, len(t)+1):
			scores = [distance[index_s-1][index_t-1] + (s[index_s-1] != t[index_t-1]),
			          distance[index_s-1][index_t] + 1,
			          distance[index_s][index_t-1] + 1]
			distance[index_s][index_t] = min(scores)

			# if the score matches the minimum, add the preceeding number of alignment
			if distance[index_s][index_t] == scores[0]:
				counts[index_s][index_t] += counts[index_s-1][index_t-1]
			if distance[index_s][index_t] == scores[1]:
				counts[index_s][index_t] += counts[index_s-1][index_t]
			if distance[index_s][index_t] == scores[2]:
				counts[index_s][index_t] += counts[index_s][index_t-1]

			# take the count modulo 2**27 -1
			counts[index_s][index_t] = counts[index_s][index_t] % ((2**27)-1)

	return counts[-1][-1]

if __name__ == '__main__':
	dataset = open(sys.argv[1]).read()
	s, t = parse_fasta(dataset).values()
	print (count_alignments(s, t))


