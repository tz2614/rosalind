#! usr/bin/env/python

"""
Problem: Introduction to Alternative Splicing
URL: http://rosalind.info/problems/aspc/

Given: Positive integers n and m with 0 <= m <= n <= 2000.
Return: The sum of combinations C(n,k) for all k satisfying m <= k <= n, modulo
1,000,000.
"""

from math import factorial
import sys

def combinations(n, m):
	return sum(factorial(n) // (factorial(k) * factorial(n-k)) for k in range(m, n+1))

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		n, m = [int(i) for i in data_file.readline().strip().split(' ')]

	answer = combinations(n, m) % 1000000
	print(answer)
