#! usr/bin/env/python


"""
Problem: Introduction to Set Operations
URL: http://rosalind.info/problems/seto/

Given: A positive integer n(n<=20,000) and two subsets A and B of {1,2...,n}.

Return: Six sets: AuB, AnB, A-B, B-A, Ac, and Bc (where set complements are 
taken with respect to {1,2,...,n}.

"""

import sys

def parse_data(line):
	
	""" parse numbers from second and third line to set a and b """

	return [num.strip() for num in line.strip()[1:-1].split(",")]


def set_operation(n, a, b):

	""" return sets required """

	return [a | b, a & b, a - b, b - a,  set(range(1, n+1)) - a, set(range(1, n+1)) - b]

def format_result(results):

	""" return results in { } format as required """

	with open('answer.txt', 'w') as outfile:

		for result in results:
			#print ("{" + ', '.join(map(str, result)) + "}")
			outfile.write("{" + ', '.join(map(str, result)) + "}\n")

if __name__ == '__main__':
	
	dataset = sys.argv[1]
	n, a, b = open(dataset).readlines()

	n = int(n.strip())
	a = set(map(int, parse_data(a)))
	b = set(map(int, parse_data(b)))

	format_result(set_operation(n, a, b))