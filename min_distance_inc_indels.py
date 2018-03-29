#! usr/bin/env python

"""
	Given: Two protein strings s and t in FASTA format (each of length at most 1000
	aa).
	
	Return: The edit distance dE(s,t).

	>>> problem('PLEASANTLY', 'MEANLY')
	5
"""

from itertools import product
import sys

def parse_fasta(dataset):

    """
    Parses data in FASTA format, returning a dictionary of ID's and values
    """

    records = {}
    record_id = None

    for line in [lines.strip() for lines in dataset.splitlines()]:
        
        if line.startswith('>'):
            records_id = line[1:]
            records[records_id] = ""
        else:
            records[records_id] += line
            #print records
    
    return records

def min_distance(seq1, seq2):

    distance = {}

    distance.update({((i, 0), i) for i in range(len(seq1) + 1)})
    distance.update({((0, i), i) for i in range(len(seq2) + 1)})
  
    for index_1, index_2 in product(range(1, len(seq1)+1), range(1, len(seq2)+1)):

        if seq1[index_1-1] == seq2[index_2-1]:
            cost = 0
        else:
            cost = 1
            
        distance[(index_1, index_2)] = min(distance[(index_1-1, index_2-1)] + cost, distance[(index_1-1, index_2)] + 1, distance[(index_1, index_2-1)] + 1)

    return distance[(index_1, index_2)]

if __name__ == '__main__':

	dataset = open(sys.argv[1]).read()
	dataset = parse_fasta(dataset)
	s, t = dataset.values()
	print (min_distance(s, t))