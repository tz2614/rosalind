#! usr/bin/env python

"""
Problem: Wobble Bonding and RNA Secondary Structures
URL: http://rosalind.info/problems/rnas/

Given: An RNA string s (of length at most 200 bp).

Return: The total number of distinct valid matchings of basepair edges in the 
bonding graph of s. Assume that wobble base pairing is allowed.
"""

import sys

def pair(seq):

	# only one possible match for a seq of length one.
	if len(seq) < 4:
		return 1

	# no need to recalculate a sequence if we've already done so.
	if seq in prev:
		return prev[seq]

	# Otherwise, do the calculation and add it to the dictionary

	else:
		prev[seq] = pair(seq[1:])

		for i in range(4, len(seq)):
			if seq[i] in match[seq[0]]:
				prev[seq] += pair(seq[1:i]) * pair(seq[i+1:])

	return prev[seq]

if __name__ == "__main__":
	# read input sequence.
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		seq = data_file.read().replace('\n', '')

	# The possible basepair matchings including wobble base pairing.
	match = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}

	# keep track of the number of the valid pairs.

	prev = {}

	print(pair(seq))


