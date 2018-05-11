#! usr/bin/env python

"""
Problem: Constructing a De Bruijn Graph
URL: http://rosalind.info/problems/dbru/

Given: A collection of up to 1000 DNA strings of equal length (not exceeding 
50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding 
to S u Src.
"""

import sys

def reverse_complement(s):
	rev_comp = ""
	for c in s[::-1]:
		rev_comp += "ATGC"["TACG".find(c)]
	return rev_comp

if __name__ == "__main__":
	dataset = sys.argv[1]
	t = [x.strip() for x in open(dataset).readlines()]
	f = open('answer.txt', 'w')
	s = []
	c = {}

	for e in t:
		s.append(e)
		s.append(reverse_complement(e))

	for i in range(len(s)):
		c[s[i][:len(s[i])-1], s[i][1:]] = 1

	for e in c:
		f.write(str(e).replace("'", ''))
		f.write('\n')

	f.close()

