#! usr/bin/env python

"""
Problem: Counting Disease Carriers
URL: http://rosalind.info/problems/afrq/

Given: An array A for which A[k] represents the proportion of homozygous
recessive individuals for the k-th Mendelian factor in a diploid population.
Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the
probability that a randomly selected individual carries at least one copy of
the recessive allele for the k-th factor.
"""

from math import sqrt
import sys

def probability(i):
	# f(aa) = p**2
	# i = p**2
	# p = sqrt(i)
	p = sqrt(i)

	# 1 = f(AA) + f(Aa) + f(aa)
	# 1 = p**2 + 2pq + q**2
	# 1 = (p + q)**2
	# sqrt(1) = p + q
	# q = 1 - p
	q = 1 - p

	# P(Aa or aa) = 2pq + p**2
	prob = 2*p*q + i

	return prob

if __name__ == "__main__":
	dataset = sys.argv[1]
	# Read the list of frequencies
	with open(dataset, 'r') as data_file:
		a = [float(i) for i in data_file.read().strip().split(' ')]

	# calculate the probability for each one.
	prob = [probability(i) for i in a]

	# output the answer
	print ' '.join("{:.3f}".format(i) for i in prob)
	

