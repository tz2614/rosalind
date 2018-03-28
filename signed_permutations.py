#! usr/bin/env python

"""
	Given: A positive integer n<=6.

	Return: The total number of signed permutations of length n, 
	followed by a list of all such permutations (you may list the signed permutations in any order).

>>> format(problem(2))
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
"""

from itertools import permutations, product
import sys

def signed_permutations(n):
	nums = range(1, n + 1)
	perms = []
	for perm in permutations(nums):
		for signs in product([-1, 1], repeat=n):
			yield map(lambda x: x[0] * x[1], zip(signs, perm))

if __name__ == '__main__':

	n = int(open(sys.argv[1]).read())
	num_perms = len(list(signed_permutations(n)))
	print num_perms
	for perm in signed_permutations(n):
		print ' '.join(map(str, perm))
