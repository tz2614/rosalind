#! usr/bin/env python

"""
    http://rosalind.info/problems/lexv/

    Given: A permutation of at most 12 symbols defining an ordered alphabet A
    and a positive integer n(n<=12).
    
    Return: All strings of length at most n formed from A, ordered
    lexicographically. (Note: As in "Enumerating k-mers Lexicographically",
    alphabet order is based on the order in which the symbols are given.)
"""

from itertools import chain, product
from functools import cmp_to_key
import sys

def order_by_lex_vlen(dataset):

	# parse input from dataset
	alphabet, n = (dataset[:-1], int(dataset[-1]))

	# define a table and comparison function for the alphabet
	table =  dict((char, index) for index, char in enumerate(alphabet))

	def compare (a, b):
		for i in range(max(len(a), len(b)) + 1):
			try:
				diff = table[a[i]] - table[b[i]]
				if diff == 0:
					continue
				return diff
			except IndexError:
				if i not in a:
					return 1
				if i not in b:
					return -1
		
		return 0

	# return sorted chars
	chars = chain(*[product(alphabet, repeat=i) for i in range(1, n + 1)])
	return sorted(chars, key=cmp_to_key(compare))

if __name__ == '__main__':

	dataset = open(sys.argv[1]).read().strip().split()
	print '\n'.join(map(''.join, order_by_lex_vlen(dataset)))
