#! usr/bin/env python

"""
Problem: Matching Random Motifs
URL: http://rosalind.info/problems/rstr/

Given: A positive integer N <= 100000, a number x between 0 and 1, and a DNA
string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as
s are constructed with GC-content x (see "Introduction to Random Strings"), then
at least one of the strings equals s. We allow for the same random string to be
created more than once.
"""

"""
EXAMPLE INPUT:
90000 0.6
ATAGCCGA

EXAMPLE OUTPUT:
0.689
"""

import sys

def random_motif(n, gc, seq):

	prob_gc = gc/2
	prob_at = (1-gc)/2
	percent = 1

	for j in range(len(seq)):

		nt = seq[j]
		
		if nt in 'GC':
			percent *= prob_gc
		elif nt in 'AT':
			percent *= prob_at

	percent = 1 - (1-percent)**n

	return percent

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset) as data_file:
		n, seq = data_file.read().strip().split('\n')
		n, gc = n.split(' ')
		n = int(n)
		gc = float(gc)

	print ("{:.3f}".format(random_motif(n, gc, seq)))



