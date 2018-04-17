#! usr/bin/env python

"""
Problem: Counting Subsets
URL: http://rosalind.info/problems/sset/

Given: A positive integer n (n <= 1000).

Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.
"""

import sys

def counting_subset(dataset):
	with open (dataset) as data_file:
		n = int(data_file.read())

	return (2**n % 1000000)

if __name__ == '__main__':
	dataset = sys.argv[1]
	print (counting_subset(dataset))