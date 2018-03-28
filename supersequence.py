#! usr/bin/env python

"""
Given: Two DNA strings s and t.

Return: A shortest common supersequence of s and t. If multiple solutions
exist, you may output any one.

>>> supersequence('ATCTGAT', 'TGCATA')
'ATGCATGAT'
"""

import sys

def supersequence(s, t):

	commonseq = lcs(s, t)
	s, t = [line.strip() for line in dataset]
	#print commonseq
	superseq = ""
	index_s = 0
	index_t = 0
	
	for base in commonseq:
		
		if index_s < len(s):
			while s[index_s] != base:
				superseq += s[index_s]
				index_s += 1
			index_s += 1

		if index_t < len(t):
			while t[index_t] != base:
				superseq += t[index_t]
				index_t += 1
			index_t += 1

		superseq += base

	if index_s < len(s):
		superseq += s[index_s:]
	if index_t < len(t):
		superseq += t[index_t:]
	return superseq

dataset = open(sys.argv[1]).readlines()
s, t = [line.strip() for line in dataset]
print supersequence(s, t)
