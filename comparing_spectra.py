#! usr/bin/env python

"""
Problem: Comparing Spectra with the Spectral Convolution
URL: http://rosalind.info/problems/conv/

Given: Two multisets of positive real numbers S1 and S2. The size of each 
multiset is at most 200.

Return: The largest multiplicity of S1-S2, as well as the absolute value of 
the number x maximizing (S1-S2)(x) (you may return any such value if multiple 
solutions exist).
"""

from decimal import Decimal
import sys

def largest_multiplicity(s, t):
	# calculate teh Minkowski difference from both sets.

	sets = {}
	for i in s:
		for j in t:
			d = i - j
			if d in sets:
				sets[d] += 1
			else:
				sets[d] = 1

	# find the largest multiplicity and return it.
	largest = max((v, k) for k, v in sets.items())

	return largest

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		s, t = [[Decimal(x) for x in line.split()] for line in data_file.read().strip().split('\n')]

	print('\n'.join(map(str, largest_multiplicity(s, t))))