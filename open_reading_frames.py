#! usr/bin/env python

"""
Problem: Open Reading Frames
URL: http://rosalind.info/problems/orf/

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.

>>> dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
>>> r = problem(dna)
>>> format(r)
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""


import re
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

def codon_table(seq_type='rna'):
    ''' Return a dictionary of codons and corresponding amino acids '''
    bases = ['U', 'C', 'A', 'G'] if seq_type == 'rna' else ['T', 'C', 'A', 'G']
    
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codons = [a+b+c for a in bases for b in bases for c in bases]
    codon_table = dict(zip(codons, amino_acids))

    return codon_table

def reverse_complement(seq):
    ''' Return the reverse complement of a given DNA or RNA string. '''
    if 'U' in seq:
        seq_dict = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    else:
        seq_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

    return ''.join([seq_dict[base] for base in reversed(seq)])

def translate(seq):
	''' Translate all 6 ORFs (3 for the forward strand, 3 for the reverse). '''
	table =  codon_table('dna')
	peptides = ['' for i in range(6)]
	rev = reverse_complement(seq)

	for i in range(3):
		for j in range(i, len(seq), 3):
			codon = seq[j:j+3]
			peptides[i] += table.get(codon, '-')
		for j in range(i, len(rev), 3):
			codon = rev[j:j+3]
			peptides[i+3] += table.get(codon, '-')

	return peptides

def find_orfs(peptides):
	starts = []
	pep_list = []

	# Identify the position of each Methionine (corresponding to a start codon)
	for i in range(len(peptides)):
		for j in range(len(peptides[i])):
			if peptides[i][j] =='M':
				starts.append([i, j])

	# from each identified start position, search for an interval from 'M' to
	# a stop codon ('*') corresponding to a possible peptide
	for j in starts:
		p = peptides[j[0]]
		p = p[j[1]:len(p)]
		q = re.search('M[A-Z]*\*', p)
		if q != None:
			pep_list.append(q.group().rstrip('*')) # strip the stop codon

	return list(set(pep_list)) # use set() to elimnate any duplicates

if __name__ == '__main__':
	
	seq = parse_fasta(sys.argv[1])

	peptides = translate(seq)

	orfs = find_orfs(peptides)

	print '\n'.join(orfs)

