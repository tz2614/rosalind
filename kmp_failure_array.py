#! usr/bin/env python

"""
Problem: Speeding Up Motif Finding 
URL: http://rosalind.info/problems/kmp/
Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.


EXAMPLE INPUT:
>Rosalind_87
CAGCATGGTATCACAGCAGAG

EXAMPLE OUTPUT:
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

import sys

def parse_fasta(path, no_id=True):
    ''' Read in a Fasta file. If no_id is set to False, return a dictionary of
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

def failure_array(s):
	# pre-populate array with 0s
	failure_array = [0 for i in range(len(s))]
	n = len(s) # length of array
	k = 1 # position in the string
	j = 0 # length of the longest substring

	while k < n:
		if s[k] == s[j]:
			j += 1
			failure_array[k] = j
			k += 1
		else:
			if j != 0:
				j = failure_array[j-1]
			else:
				failure_array[k] = 0
				k += 1
	return failure_array

if __name__ == "__main__":
	dataset = sys.argv[1]
	s = parse_fasta(dataset)
	with open("answer.txt", 'w') as outfile:
		outfile.write(' '.join(map(str, failure_array(s))))





