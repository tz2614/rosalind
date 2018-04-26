#! usr/bin.env python

"""
Problem: Motzkin Numbers and RNA Secondary Structures
URL: http://rosalind.info/problems/motz/

Given: An RNA string s of length at most 300 bp.

Return: The total number of noncrossing matchings of basepair edges in the 
bonding graph of s, modulo 1,000,000
"""

import sys

def motz_number(seq):

	match = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
	prev = {}
    
    #Return the number of noncrossing matchings of basepair edges.
	if len(seq) <= 1:
		return 1
	#avoid recalculating a sequence if we already done so.
	if seq in prev:
		return prev[seq]

	#otherwise do the calculation and add it to the dictionary.
	else:
		prev[seq] = motz_number(seq[1:])

		for i in range(1, len(seq)):
			if seq[i] == match[seq[0]]:
				prev[seq] += motz_number(seq[1:i]) * motz_number(seq[i+1:])

	return prev[seq]

if __name__ == "__main__":

	dataset = sys.argv[1]
	with open(dataset) as data_file:
		data_file.readline()
		seq = data_file.read().replace("\n", "").replace('\r', '')


	print (motz_number(seq) % 1000000)

