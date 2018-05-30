#! usr/bin/env python

"""
Problem Title: Encoding Suffix Trees
Rosalind ID: SUFF
Rosalind #: 074
URL: http://rosalind.info/problems/suff/
"""

import sys

class Node:
    def __init__(self):
        self.s = {}

    def __repr__(self):
        return 'Node (d=%s)' % self.s

def suffix_tree(t, l):
    if len(t.s) == 1:
        for x in t.s:
            l.append(x)
            suffix_tree(t.s[x], l)
    else:
        if l:
            output.write(''.join(l) + '\n')
            print ''.join(l)
        for x in t.s:
            suffix_tree(t.s[x], [x])

def get_substrings(s):
    root = Node()
    
    for i in xrange(len(s)):
        cur = root
        
        for c in s[i:]:
            if not c in cur.s:
                cur.s[c] = Node()
                
            cur = cur.s[c]

    suffix_tree(root, None)

if __name__ == '__main__':

	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		s = data_file.readline().strip()

	output = open('answer.txt','w')
	get_substrings(s)
	output.close()