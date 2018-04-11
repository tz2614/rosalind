#! usr/bin/env python

'''
Problem: Counting Phylogenetic Ancestors
URL: http://rosalind.info/problems/inod/

Given: A positive integer n (3 <= n <= 10000).

Return: The number of internal nodes of any unrooted binary tree having n leaves.
'''

# Rooted vs Unrooted:
# - A rooted binary tree with n leaves has 2n-2 edges, and n-1 internal nodes.
# - An unrooted binary tree with n leaves has 2n-3 edges and n-2 internal nodes
# (picture the root of a tree and it's two edges combining into a single edge).

import sys

def num_of_internal_nodes(dataset):

	with open(dataset) as data_file:
		n = int(data_file.read())

	return (n-2)

if __name__ == '__main__':

	dataset = sys.argv[1]
	print (num_of_internal_nodes(dataset))



