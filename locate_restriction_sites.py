#! usr/bin/env python

"""
Problem: Locating Restriction Sites
URL: http://rosalind.info/problems/revp/

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having
length between 4 and 12. You may return these pairs in any order.
"""

import sys
from string import maketrans

def rev_comp(dna):

    """Create a DNA string that is in reverse order and complementary using argument provided as input
        Args:
        DNA (str): DNA string to reverse
        Returns:
        reverse complement sequence of DNA string
    """
    return dna[::-1].translate(maketrans('ATCG', 'TAGC'))

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

def locate_rest_sites(dna):
	for length in range(4, 13):
		for site in range(len(dna) - length + 1):
			if seq[site:site+length] == rev_comp(dna[site:site+length]):
				yield site, dna[site:site+length]

if __name__ == '__main__':
	dataset = open(sys.argv[1]).read()
	for seq in parse_fasta(dataset).values():
		for index, dna in sorted(locate_rest_sites(seq)):
			print index + 1, len(dna)
