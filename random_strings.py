#! usr/bin/env python

""" 
Problem: Introduction to Random Strings
URL: http://rosalind.info/problems/prob/

Given: A DNA string s of length at most 100 bp and an array A containing at 
most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the
common logarithm of the probability that a random string constructed with the
GC-content found in A[k] will match s exactly.
"""

from math import log10
import sys

def random_string_prob(seq, gc):
	
	log_p = []

	for i in range(len(gc)):
		prob_gc = gc[i]/2
		prob_at = (1-gc[i])/2
		prob = 1

		for j in range(len(seq)):

			nt = seq[j]
			
			if nt in 'GC':
				prob *= prob_gc
			elif nt in 'AT':
				prob *= prob_at

		prob = log10(prob)
		log_p.append(prob)

	return log_p

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset) as data_file:
		seq, gc = data_file.read().strip().split('\n')
		gc = [float(x) for x in gc.split(' ')]

	answer = random_string_prob(seq, gc)

	print (' '.join(['{:.3f}'.format(i) for i in answer]))