#!/usr/bin/env python	

"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one).

>>> lcs('AACCTTGG', 'ACACTGTGA')
AACTGG
"""

import sys


def fasta_parser(dataset):
    with open (dataset) as fasta_filehandle: 
        # count keeps track of the number of DNA strings
        count = 0
        s = ""
        t = ""

        for line in fasta_filehandle:
            line = line.strip()
            
            if line.startswith(">"):
                count += 1  
            # create the DNA string
            elif count == 1:
                s += line
            # create the intron string
            elif count > 1:
                t += line
        return s, t

        #print "DNA sequence s = {}".format(s) 
        #print 
        #print "DNA sequence t = {}".format(t)
        #print

def lcs(s, t):
    lengths = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

    for index_s, base_s in enumerate(s):
        for index_t, base_t in enumerate(t):
            if base_s == base_t:
                lengths[index_s+1][index_t+1] = lengths[index_s][index_t] + 1
            else:
                lengths[index_s+1][index_t+1] = \
                    max(lengths[index_s+1][index_t], lengths[index_s][index_t+1])

    result = []
    x, y = len(s), len(t)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert s[x-1] == t[y-1]
            result = [s[x-1]] + result
            x -= 1
            y -= 1

    return ''.join(result)

if __name__ == '__main__':

	dataset = fasta_parser(sys.argv[1])
	print ''.join(map(str, lcs(dataset)))