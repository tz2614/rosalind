#! usr/bin/env python

"""
    http://rosalind.info/problems/lexf/

    Given: A collection of at most 10 symbols defining an ordered alphabet, and
	a positive integer n (n<=10).

    Return: All strings of length n that can be formed from the alphabet,
    ordered lexicographically.
"""

from itertools import product
from functools import cmp_to_key
import sys

def order_perm_lex(dataset):
	
	# parse input from dataset
	alphabet, n = (dataset[:-1], int(dataset[-1]))

	# define a table and comparison function for the alphabet
	table = dict((char, index) for index, char in enumerate(alphabet))

	def compare (a, b):
		for i in range(len(a) + 1):
			diff = table[a[i]] - table[b[i]]
			if diff == 0:
				continue
			return diff
		return 0

	# return sorted alphabet
	return sorted(product(alphabet, repeat=n), key=cmp_to_key(compare))

if __name__ == '__main__':

	dataset = open(sys.argv[1]).read().strip().split()
	print '\n'.join(map(''.join, order_perm_lex(dataset)))

