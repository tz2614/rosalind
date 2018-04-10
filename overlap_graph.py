#! usr/bin/env python

"""
Problem: Overlap Graphs
URL: http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at most
10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any
order.
"""

import sys

def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = {}
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
            records[record_id] = ""
        else:
            records[record_id] += line
    return records

def overlap_seqs(dataset):
	for id1, seq1 in dataset.items():
		suffix = seq1[-3:]
		for id2, seq2 in dataset.items():
			prefix = seq2[:3]
			if seq1 != seq2:
				if suffix == prefix:
					yield(' '.join([id1, id2]))

if __name__ == '__main__':
	dataset = parse_fasta(open(sys.argv[1]).read())
	for seq in overlap_seqs(dataset):
		print (seq)
