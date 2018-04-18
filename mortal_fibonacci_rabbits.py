#!usr/bin/env python

"""
Problem: Mortal Fibonacci Rabbits
URL: http://rosalind.info/problems/fibd/

Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
"""

import sys

def rabbits(n, m):
	""" where n is the number of months, m is the longevity of rabbits in month(s) """

	""" start with one pair of rabbits where [1, 0, 0, 0...] """
	rabbits = [1] + (m - 1) * [0]

	for i in range(n-1):
		new_rabbits = sum(rabbits[1:])
		rabbits = [new_rabbits] + rabbits[:-1]
	return sum(rabbits)

if __name__ == '__main__':
	
	dataset = sys.argv[1]
	
	with open(dataset) as data_file:
		n, m = [int(i) for i in data_file.read().strip().split(' ')]

	print (rabbits(n, m))