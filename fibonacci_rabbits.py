#! usr/bin/env python

""" 
Problem: Rabbits and Recurrence Relations
URL: http://rosalind.info/problems/fib/
Positive integers n <= 40 and k <= 5.

Return: The total number of rabbit pairs that will be present after n months if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

import sys

def fib_growths(n, k):
	if n <= 1:
		return 1
	else:
		return fib_growths(n-1, k) + fib_growths(n-2, k) * k

if __name__ == '__main__':
	
	dataset = sys.argv[1]
	
	with open (dataset, 'r') as data_file:
		n, k = [int(i) for i in data_file.read().strip().split(' ')]

	""" given that n = 0 refers to the first month, the number of rabbits
	present after n months hence refers to n-1 months. """

	print (fib_growths(n-1, k))