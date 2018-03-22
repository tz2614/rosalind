#!usr/bin/env python


"""
For DNA strings s and t having the same length, their transition/transversion
ratio trans_trans(s, t) is the ratio of the total number of transitions to the total
number of transversions, where symbol substitutions are inferred from
mismatched corresponding symbols as when calculating Hamming distance (see
'Counting Point Mutations').

Given: Two DNA strings s and t of equal length (at most 1 kbp).

Return: The transition/transversion ratio trans_trans(s, t).

>>> s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
>>> s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
>>> round(trans_trans(s, t), 11)
1.21428571429
"""

import sys

def trans_trans(dataset):

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

	transitions = set([("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")])
	
	ratio = {True: 0.0, False: 0.0}
	
	for pair in zip(s, t):
		
		if pair[0] != pair[1]:
			ratio[pair in transitions] += 1
	
	return ratio[True] / ratio[False]

dataset = sys.argv[1]
print trans_trans(dataset)

