#! usr/bin/env python

"""
	Given: Positive integers n and k such that 100>=n>0 and 10>=k>0.
	Return: The total number of partial permutations P(n,k) modulo 1000000.
	
	>>> problem(21, 7)
	51200
"""

from math import factorial
import sys

def part_perm(dataset):
	# P(n,k) = n!/(n-k)!
	n, k = map(int, dataset.split())
	return factorial(n) / factorial(n-k) % 1000000

if __name__ == '__main__':
	dataset = open(sys.argv[1]).read().strip()
	print part_perm(dataset)
