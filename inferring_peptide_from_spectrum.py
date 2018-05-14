#! usr/bin/env python

"""
Problem: Inferring Peptide from Full Spectrum
URL: http://rosalind.info/problems/full/

Given: A list L containing 2n+3 positive real numbers (n<=100). The first number 
in L is the parent mass of a peptide P, and all other numbers represent the 
masses of some b-ions and y-ions of P (in no particular order). You may assume 
that if the mass of a b-ion is present, then so is that of its complementary 
y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real 
numbers w1 and w2 such that for every prefix p and suffix s of t, each of 
w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists 
a protein string whose t-prefix and t-suffix weights correspond to the 
non-parent mass values of L.) If multiple solutions exist, you may output any 
one.
"""

import sys

def mass_to_aa(val, tolerance=0.0001):
    ''' Returns the amino acid corresponding to a given mass. '''
    
    # The monoisotopic masses of each 
    aa_table = { 71.03711:'A',
                 103.00919:'C',
                 115.02694:'D',
                 129.04259:'E',
                 147.06841:'F',
                 57.02146:'G',
                 137.05891:'H',
                 113.08406:'I',
                 128.09496:'K',
                 113.08406:'L',
                 131.04049:'M',
                 114.04293:'N',
                 97.05276:'P',
                 128.05858:'Q',
                 156.10111:'R',
                 87.03203:'S',
                 101.04768:'T',
                 150.95363:'U',
                 99.06841:'V',
                 186.07931:'W',
                 163.06333:'Y' }
    
    # Keep track of the closest match to the given mass. Admittedly this is 
    # only useful in certain circumstances...
    closest = ['', 999]
    
    for mass, aa in aa_table.items():
        diff = abs(val - mass)
        if diff < closest[1]:
            closest = [aa, diff]
            
        # Return if a match is found.
        if diff < tolerance:
            return aa

    # Print a warning message if no match is found.
    # print('Note: Could not find an amino acid with monoisotopic mass %.5f.' % val)
    # print(' '*6 + 'Closest match is', closest[0], '(mass difference %5f).' % closest[1])

def build_peptide(n, frag_dict, peptide='', aa=0):
	""" Given a dictionary of fragment masses, with the next highest fragment
	mass and an amino acid representing the gap between them, iterably build a 
	peptide by starting with the smallest mass.
	"""

	if aa == 0:
		aa = min(frag_dict)

	if len(peptide) == n:
		return peptide
	else:
		for i in frag_dict[aa]:
			return build_peptide(n, frag_dict, peptide+i[0], i[1])

def peptide_from_frag(p, masses_of_l):
	# A peptide has length n, assuming a list of 2n+2 masses are given
	# (excluding the mass of the parent peptide)

	n = (len(masses_of_l)-2)/2

	# Find each pair of b- and y- ions.

	pairs = {}
	for i in range(len(masses_of_l)):
		for j in range(i, len(masses_of_l)):
			aa = mass_to_aa(masses_of_l[j]-masses_of_l[i])
			if aa:
				if masses_of_l[i] in pairs:
					pairs[masses_of_l[i]].append((aa, masses_of_l[j]))
				else:
					pairs[masses_of_l[i]] = [(aa, masses_of_l[j])]

	# Iterably build the peptide starting with the smallest fragment mass.
	peptide = build_peptide(n, pairs)

	# Return the completed peptide of length of n.
	return peptide

if __name__ == "__main__":
	dataset = sys.argv[1]
	with open(dataset, 'r') as data_file:
		p = float(data_file.readline().strip())
		frags = list(map(float, data_file.readlines()))

	print(peptide_from_frag(p, frags))


