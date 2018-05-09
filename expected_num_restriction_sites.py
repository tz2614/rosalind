#! usr/bin/env/python

"""
Problem: Expected Number of Restriction Sites
URL: http://rosalind.info/problems/eval/

Given: A positive integer n (n <= 1,000,000), a DNA string s of even length at
most 10, and an array A of length at most 20, containing numbers between 0 and
1.

Return: An array B having the same length as A in which B[i] represents the
expected number of times that s will appear as a substring of a random DNA
string t of length n, where t is formed with GC-content A[i]

(see "Introduction to Random Strings").
"""

import sys

def gc_percent(seq, gc):
	prob_gc = gc/2
	prob_at = (1-gc)/2
	percent = 1

	for j in range(len(seq)):
		nt = seq[j]
		if nt in 'GC':
			percent *= prob_gc
		elif nt in 'AT':
			percent *= prob_at

	return (percent) 

def expected_prob_restriction_sites(n, s, a):
	for i in a:
		prob = gc_percent(s, i) * (n-1)
		yield(prob)

if __name__ == "__main__":

	dataset = sys.argv[1]
	with open (dataset, 'r') as data_file:
		n, s, a = data_file.read().strip().split('\n')
		n = int(n)
		a = [float(i) for i in a.split(' ')]

	print (' '.join(["{:.3f}".format(p) for p in expected_prob_restriction_sites(n, s, a)]))

