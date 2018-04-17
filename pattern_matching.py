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

from itertools import count
import sys

class Trie(object):
    def __init__(self):
        self.counter = count(start = 1)
        self.root = [next(self.counter), {}]

    def insert(self, bp):
        node = self.root
        for ch in bp:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter), {}]
            
            node = node[1][ch]

def format_output(node):
    for ch, node2 in node[1].iteritems():
        print node[0], node2[0], ch
        format_output(node2)
        
def get_adjency_list(bps):
    trie = Trie()
    for bp in bps:
        trie.insert(bp)
    return trie.root

if __name__ == '__main__':
    dataset = open(sys.argv[1]).readlines()
    dataset = [l.strip() for l in dataset if l.strip()]
    
    with open('answer.txt', 'w') as outfile:
    	outfile.write(format_output(get_adjency_list(dataset)))