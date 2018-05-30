#! usr/bikn/env python

"""
Problem: Counting Unrooted Binary Trees
URL: http://rosalind.info/problems/cunr/
Given: A positive integer n (n<=1000).
Return: The value of b(n) modulo 1,000,000.
"""

import sys

if __name__ == "__main__":
	# quick function to calculate the double factorial of a given number
	doublefactorial = lambda n: n * doublefactorial(n-2) if n > 1 else 1

	# read the number of leaves, n.
	n = int(open(sys.argv[1], 'r').read())

	# the number of trees on n leaves s the double factorial, (2n-5)!!
	print (doublefactorial(2*n-5) % 1000000)