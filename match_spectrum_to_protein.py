#! usr/bin/env python

"""
Problem: Matching a Spectrum to a Protein
URL: http://rosalind.info/problems/prsm/

Given: A positive integer nn followed by a collection of nn protein strings 
s1s1, s2s2, ..., snsn and a multiset RR of positive numbers (corresponding to 
the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R(rho)S[sk] taken over all strings sk, 
followed by the string sk for which this maximum multiplicity occurs (you may 
output any such value if multiple solutions exist).
"""

import operator
import sys
from collections import Counter

def get_values(set1, set2, oper = operator.add):
	return [round(oper(s1, s2), 5) for s1 in set1 for s2 in set2]

def get_largest_multiplicity(s1, s2):
	diff = [abs(r) for r in get_values(s1, s2, oper = operator.sub)]
	multiplicity = Counter(diff)

	return multiplicity.most_common()[0][::-1]

def get_substrings(string):
	for i in range(len(string)):
		if i != len(string) - 1:
			yield string[:i+1]
		yield string[-i:]

def protein_weight(protein):
	mass_dict = {'A': 71.03711, 'C':103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 
                 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
                 'M': 131.04049, 'N': 114.04293, 'P':97.05276, 'Q': 128.05858, 'R': 156.10111,
                 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
	return sum(mass_dict[p] for p in protein)

def get_max_multiplicity(proteins, rset):
	output = [0, None]
	for protein in proteins:
		pset = [protein_weight(p) for p in get_substrings(protein)]
		most, _ = get_largest_multiplicity(rset, pset)

		if most >= output[0]:
			output[0] = most
			output[1] = protein
	return output

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		n = int(data_file.readline().rstrip())
		proteins = [data_file.readline().rstrip() for i in range(n)]
		rset = [round(float(r.rstrip()), 5) for r in data_file.readlines()]

	print ("\n".join(str(x) for x in get_max_multiplicity(proteins,rset)))