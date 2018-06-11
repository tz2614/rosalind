#! usr/bin/env python

"""
Problem: Sex-Linked Inheritance
URL: http://rosalind.info/problems/sexl/

Given: An array A of length n for which A[k] represents the proportion of 
males in a population exhibiting the k-th of n total recessive X-linked 
genes. Assume that the population is in genetic equilibrium for all n genes.

Return: An array B of length n in which B[k] equals the probability that a 
randomly selected female will be a carrier for the k-th gene.
"""

import sys

if __name__ == "__main__":
	
	# Read the list of frequencies.
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		a = [float(i) for i in data_file.read().strip().split(' ')]

	prob = [i * (1-i) / 0.5 for i in a]

	# Output the answer
	print (' '.join([str(i) for i in prob]))
	with open('answer.txt', 'w') as outfile:
		outfile.write(' '.join([str(i) for i in prob]))

