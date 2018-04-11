#! usr/bin/env python

"""
Problem: Completing a Tree
URL: http://rosalind.info/problems/tree/

Given: A positive integer n (n <= 1000) and an adjacency list corresponding to
a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a
tree.
"""

import sys

def complete_tree(dataset):
	with open(dataset) as data_file:
		n = int(data_file.readline())
		adj_list = data_file.readlines()

	answer = n - len(adj_list) - 1

	print(answer)

if __name__ == '__main__':
	dataset = sys.argv[1]
	complete_tree(dataset)