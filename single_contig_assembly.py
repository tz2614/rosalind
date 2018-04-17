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

def parse_fasta(path, no_id=True):
    ''' Read in a Fasta file. If no_id is set to False, return a dictonary of
        sequences with associated headers; otherwise return a list of 
        sequences only.
    '''
    ids = []
    seqs = []
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))

def match_seq(seq, seq_list):
	""" starting with length len(seq)-1, look for iteratively smaller and 
		smaller areas of overlap with other sequences until just over half len(seq).
		Stops at the first case of overlap, returns a superstring combining the two sequences.
	"""
	half = int(len(seq)/2)
	#print half

	for i in range(len(seq)-1, half, -1):
		overlap = seq[len(seq)-i:]
		#print overlap

		for seq2 in seq_list:
			#print seq2
			if seq2 != seq:
				if seq2[:i] == overlap:
					#print seq[:(len(seq)-1)] + seq2
					return seq[:len(seq)-i] + seq2

def shortest_contig(seq_list):
	""" Iteratively create overlapping superstrings until only one is left
		(i.e. the shortest contig).
	"""
	while len(seq_list) > 1:
		
		new_list = []
		#print seq_list
		
		for seq in seq_list:
			if seq != None:
				match = match_seq(seq, seq_list)
			if match != None:
				new_list.append(match)

		seq_list = new_list
	return seq_list[0]

if __name__ == '__main__':
	
	# parse fasta file containing the fasta sequences to the variable seqs
	seqs = parse_fasta(sys.argv[1])

	# find the shortest superstring.
	print (shortest_contig(seqs))

