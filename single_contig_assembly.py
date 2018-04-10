#! usr/bin/env python

"""
Problem: Genome Assembly as Shortest Superstring
URL: http://rosalind.info/problems/long/

Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA 
format (which represent reads deriving from the same strand of a single linear
chromosome). The dataset is guaranteed to satisfy the following condition:
there exists a unique way to reconstruct the entire chromosome from these 
reads by gluing together pairs of reads that overlap by more than half their 
length.

Return: A shortest superstring containing all the given strings (thus
corresponding to a reconstructed chromosome).
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

def match_seq(seq, seq_list):
	""" starting with length len(seq)-1, look for iteratively smaller and 
		smaller areas of overlap with other sequences until just over half len(seq).
		Stops at the first case of overlap, returns a superstring combining the two sequences.
	"""
	half = int(len(seq)/2)

	for i in range(len(seq)-1, half, -1):
		overlap = seq[len(seq)-i:]

		for seq2 in seq_list:
			if seq2 != seq:
				if seq2[:i] == overlap:
					return seq[:len(seq)-1] + seq2

def shortest_contig(seq_list):
	""" Iteratively create overlapping superstrings until only one is left
		(i.e. the shortest contig).
	"""
	while len(seq_list) > 1:
		
		new_list = []
		
		for seq in seq_list:
			match = match_seq(seq, seq_list)
			if match != []:
				new_list.append(match)

		seq_list = new_list
		print seq_list

	return seq_list[0]

if __name__ == '__main__':
	
	# parse fasta file containing the fasta sequences to the variable seqs
	seqs = parse_fasta(open(sys.argv[1]).read())
	seq_list = []
	for seq in seqs.values():
		seq_list.append(seq)
	print (shortest_contig(seq_list))

