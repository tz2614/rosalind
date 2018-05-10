#! usr/bin/env python

"""
Problem: Inferring Protein from Spectrum
URL: http://rosalind.info/problems/spec/

Given: A list L of n (n<=100) positive real numbers.

Return: A protein string of length n-1 whose prefix spectrum is equal to L (if
multiple solutions exist, you may output any one of them). Consult the
monoisotopic mass table.
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
    print('Note: Could not find an amino acid with monoisotopic mass %.5f.' % val)
    print(' '*6 + 'Closest match is', closest[0], '(mass difference %5f).' % closest[1])

def cal_protein(list_of_mass):
	prot = ""
	for i in range(1, len(list_of_mass)):
		prot += mass_to_aa(list_of_mass[i]-list_of_mass[i-1])

	return prot

if __name__ == "__main__":
	
	dataset = sys.argv[1]
	# read in the list of prefix weights
	with open(dataset, 'r') as data_file:
		list_of_mass = list(map(float, data_file.read().strip().split('\n')))

	print(cal_protein(list_of_mass))


