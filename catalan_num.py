#! usr/bin/env python

"""
Problem: Catalan Numbers and RNA Secondary Structures
URL: http://rosalind.info/problems/cat/

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and
the same number of occurrences of 'C' as 'G'. The length of the string is at
most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in
the bonding graph of s, modulo 1,000,000.
"""

import sys

def count_pairings(i, j):

	if pairs[i][j] != -1:
		return(pairs[i][j])

	result = 0
	if i > j:
		result = 1
	elif j == 1 and match[seq[i] == seq[j]]:
		result = 1
	else:
		for k in range(i+1, j+1, 2):
			if seq[k] == match[seq[i]]:
				result += count_pairings(i+1, k-1) * count_pairings(k+1, j)

	pairs[i][j] = result
	return result

if __name__ == '__main__':

	dataset = sys.argv[1]
	with open(dataset) as data_file:
		data_file.readline()
		seq = data_file.read().replace('\r', '').replace('\n', '')

	match = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}

	#creating a matrix of half of seq on one axis, the other half on the other axis.

	pairs = [[-1 for x in range(len(seq)+1)] for y in range(len(seq)+1)]

	print (count_pairings(0, len(seq)-1) % 1000000)
