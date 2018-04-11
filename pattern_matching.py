#! usr/bin/env python

"""
Problem: Introduction to Pattern Matching
URL: http://rosalind.info/problems/trie/

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which
is a prefix of another.

Return: The adjacency list corresponding to the trie T for these patterns, in
the following format. If T has n nodes, first label the root with 1 and then
label the remaining nodes with the integers 2 through n in any order you like.
Each edge of the adjacency list of T will be encoded by a triple containing the
integer representing the edge's parent node, followed by the integer
representing the edge's child node, and finally the symbol labeling the edge.
"""

import sys

class Node:
	mark_overall = 0

	def __init__(self):
		self.s = {}
		Node.mark_overall += 1
		self.mark = Node.mark_overall

	def __repr__(self):
		return 'Node (mark={}, d={})'.format(self.mark, self.s)

def make_list(strings):
	root = Node()

	for x,s in enumerate(strings, 1):
		current = root
		for c in s:
			if c not in current.s:
				current.s[c] = Node()
			current = current.s[c]

	return root

def format_answer(root, answer=[]):
	for x in root.s:
		answer.append((root.mark, root.s[x].mark, x))
		format_answer(root.s[x], answer)

	return answer

if __name__ == '__main__':

	dataset = sys.argv[1]
	with open(dataset) as data_file:
		strings = data_file.read().strip().split('\n')

	root = make_list(strings)

	with open('answer.txt', 'w') as outfile:
		for i in format_answer(root):
			answer = ' '.join(map(str, i))
			outfile.write(answer + '\n')

