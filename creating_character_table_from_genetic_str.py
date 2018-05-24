#! usr/bin/env python

"""
Problem: Creating a Character Table from Genetic Strings
URL: http://rosalind.info/problems/cstr/

Given: A collection of at most 100 characterizable DNA strings, each of length 
at most 300 bp.

Return: A character table for which each nontrivial character encodes the 
symbol choice at a single position of the strings. (Note: the choice of 
assigning '1' and '0' to the two states of each SNP in the strings is 
arbitrary.)
"""

import sys

def char_table_from_strings(dna_list):
    '''Builds a character table from a given list of strings.'''
    
    ch_table = set()
    
    for i, ch in enumerate(dna_list[0]):
        # Mark the on/off taxa based on the ith character of each sequence.
        ch_array = [int(dna[i] == ch) for dna in dna_list]
        if 1 < sum(ch_array) < len(dna_list)-1:  # Check nontrivial.
            ch_table.add(''.join(map(str,ch_array)))

    return ch_table

if __name__ == "__main__":
	dataset = sys.argv[1]
	# Read the input data.
	with open(dataset) as data_file:
		dna_list = [line.strip() for line in data_file.readlines()]

	# Get the character table.
	character_table = char_table_from_strings(dna_list)

	# Print and save the answer
	print ('\n'.join(character_table))
	with open('answer.txt', 'w') as outfile:
		outfile.write('\n'.join(character_table))




