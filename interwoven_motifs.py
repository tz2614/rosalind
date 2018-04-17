#! usr/bin/env python

"""
Problem: Finding Disjoint Motifs in a Gene
URL: http://rosalind.info/problems/itwv/

Given: A text DNA string s of length at most 10 kbp, followed by a collection of
n (n <= 10) DNA strings of length at most 10 bp acting as patterns.

Return: An nxn matrix M for which Mj,k = 1 if the jth and kth pattern strings
can be interwoven into s and Mj,k = 0 otherwise.
"""

"""
EXAMPLE INPUT:
GACCACGGTT
ACAG
GT
CCG

EXAMPLE OUTPUT:
0 0 1
0 1 0
1 0 0
"""

""" creates an output file as answer.txt in the directory where you are running the script. """

from itertools import combinations_with_replacement as comb_r
import sys

def isit_superstring(a, b, superstr):
	""" check if two strings a and b can be interwoven into s. """

	if len(superstr) == 0:
		return True

	elif a[0] == b[0] == superstr[0]:
		return isit_superstring(a[1:], b, superstr[1:]) or isit_superstring(a, b[1:], superstr[1:])

	elif a[0] == superstr[0]:
		return isit_superstring(a[1:], b, superstr[1:])

	elif b[0] == superstr[0]:
		return isit_superstring(a, b[1:], superstr[1:])

	else:
		return False

def find_disjoint_motifs(s, patterns):
	""" Initialize the matrix that will hold 1 at position i, j if pattern[i] and 
	pattern[j] can be interwoven into a superstring in s, or 0 if they can't. """

	matrix = [[0 for j in range(len(patterns))] for i in range(len(patterns))]

	""" for each unique combination of patterns, iterate over them to find the superstring 
	that can be interwoven and check to see if it can be fit into string s. """

	for i in list(comb_r((i for i in range(len(patterns))), 2)):
		""" a is a pattern from the patterns list less than 10bp in length, 
		b is another pattern from the patterns list. """
		a = patterns[i[0]]
		b = patterns[i[1]]

		for j in range(len(s)-len(a)-len(b)+1):
			superstr = s[j:j+len(a)+len(b)]

			""" Add a character outside the alphabet to avoid out of range errors. """
			if isit_superstring(a+'$', b+'$', superstr):

				""" if patterns 1 and 3 can from a superstring, then 3 and 1 can as well. """

				matrix[i[0]][i[1]] = 1
				matrix[i[1]][i[0]] = 1
				break

	return matrix

if __name__ == '__main__':

	data_file = sys.argv[1]

	""" parse string s, and a list of patterns """
	
	with open (data_file, 'r') as seq_data:
		s = seq_data.readline().strip()
		#print s
		patterns = seq_data.read().strip().splitlines()
		print patterns

	""" build and populate the matrix using find_disjoint_motifs function """

	matrix = find_disjoint_motifs(s, patterns)

	""" output matrix as answer in required format """

	with open('answer.txt', 'w') as outfile:
		for i in matrix:
			outfile.write(' '.join(map(str, i)) + '\n')

