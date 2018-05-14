#! usr/bin/env python

"""
Problem: Independent Segregation of Chromosomes
URL: http://rosalind.info/problems/indc/

Given: A positive integer n<=50.

Return: An array A of length 2n in which A[k] represents the common logarithm 
of the probability that two diploid siblings share at least k of their 2n 
chromosomes (we do not consider recombination for now).
"""

from math import log10, factorial
import sys

def binomial_random_variable(n, k, p):
	a = factorial(n) / factorial(k) / factorial(n-k) # binomial coefficient
	b = p**k * (1-p)**(n-k)
	c = a * b

	return c

if __name__ == "__main__":
	
	# read input value as n
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		n = int(data_file.read())
	
	# A distribution showing the probability of sharing exactly k chromosomes.
	prob = [binomial_random_variable(n*2, k, 0.5) for k in range(2*n, -1, -1)]

	# A list of the common logarithm of the probabilities of sharing
	# *at least* k of n chromosomes.

	prob = [log10(sum(prob[:i])) for i in range(2*n, 0, -1)]

	# Output the answer.
	with open('answer.txt', 'w') as outfile:
		outfile.write(' '.join([str("{:.3f}".format(i)) for i in prob]))


