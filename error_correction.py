#! usr/bin/env python

"""
Problem: Error Correction in Reads
URL: http://rosalind.info/problems/corr/

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA
format. Some of these reads were generated with a single-nucleotide error. For
each read s in the dataset, one of the following applies:
    - s was correctly sequenced and appears in the dataset at least twice
      (possibly as a reverse complement);
    - s is incorrect, it appears in the dataset exactly once, and its Hamming
      distance is 1 with respect to exactly one correct read in the dataset (or
      its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". (Each
correction must be a single symbol substitution, and you may return the 
corrections in any order.)

"""

import string
import sys
import pprint

substitution = string.maketrans("ACGT", "TGCA")

def hamming_distance(reference_seq, comparison_seq):

	dist = 0

	for i in range(min(len(reference_seq), len(comparison_seq))):
		
		if reference_seq[i] != comparison_seq[i]:
			dist += 1

	return dist

def revert_str(sequence):
	return sequence[::-1].translate(substitution)

def count_appearances(string_list):
    ''' Count how many times a given DNA string occurs in a list. If the reverse
        complement of that string occurs in the list, it counts towards the
        original.
    '''
    str_count = {}

    for i in string_list:
        if i in str_count:
            str_count[i] += 1
        else:
            if revert_str(i) in str_count:
                str_count[revert_str(i)] += 1
            else:
                str_count[i] = 1
                str_count[revert_str(i)] = 1

    #pprint.pprint(str_count)
    return str_count

def error_correct(string_list):
    ''' Identify single symbol substitutions by comparing strings to a list of
        known correct strings (i.e. those that occur one or more times in the
        list).
    '''    
    counts = count_appearances(string_list)
    correct = []
    incorrect = []
    corrections = []
    
    for string in counts:
        if counts[string] > 1:
            correct.append(string)
        else:
            incorrect.append(string)

    for str_i in incorrect:
        for str_c in correct:
            if hamming_distance(str_i, str_c) < 2:
                corrections.append([str_i, str_c])

    return corrections

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

if __name__ == '__main__':
	
	string_list = parse_fasta(sys.argv[1])

	#print (string_list)

	corr = error_correct(string_list)
	#print corr

	with open('answer.txt', 'w') as outfile:
		for i in corr:
			outfile.write('->'.join(i) + '\n')



		
		
