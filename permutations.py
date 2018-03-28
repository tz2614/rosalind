#! usr/bin/env python

"""
	http://rosalind.info/problems/perm/

	Given: A positive integer n<=7.

    Return: The total number of permutations of length n, 

    followed by a list of all such permutations (in any order).

    >>> list_of_permutations(3)
    6
	1 2 3
	1 3 2
	2 1 3
	2 3 1
	3 1 2
	3 2 1
"""

from itertools import count, islice, permutations
import sys

def list_of_permutations(dataset):

	n = int(dataset)
	#print n
	perms = list(permutations(islice(count(start=1), 0, n)))
	return perms

if __name__ == '__main__':
	dataset = open(sys.argv[1]).read().strip()
	num_of_perm = len(list_of_permutations(dataset))
	print num_of_perm
	for perm in list_of_permutations(dataset):
		print ' '.join(map(str, perm))
