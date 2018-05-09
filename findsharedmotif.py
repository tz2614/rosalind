#! usr/bin/env python

"""
Find the longest common substring between collection of strings
"""

def sharedmotif(fastafile):
    #open and read fastafile
    fh = open(fastafile, "r")
    #create a list of all seqs
    
    seq_names = []
    seq_data = ""
    seq_list = []

    #for each line in the fastafile, remove all white spaces.
    for line in fh:
        line = line.rstrip()
        #if line starts with ">", add it to seq_names.
        if line.startswith(">"):
            seq_names.append(line)
            #print seq_names
             # if seq_data is not empty, add the line to seq_data string
            if seq_data:
                seq_list.append(seq_data)
                seq_data = ""
        else:    
            seq_data += line

    """ for the last sequence, as there are no more ">" in the text, the sequence
    will not be appended to seq_data, hence this extra line need to be added. """
    seq_list.append(seq_data)      

    """ check the seqs appended are ok """
    #print seq_list
    """ sort seqs according to length """

    seq_list = sorted(seq_list, key=len)
    #print seq_list
    """ assign shortest seq to a variable """
    shortestk = seq_list[0]
    #print shortestk

    kmers = []
    str_len = len(shortestk)
    
    """ Iterate over kmer lengths """
    for kmer_len in range(1, str_len+1)[::-1]:
        #print "Length", kmer_len

        """ Iterate over start position for that kmer length """
        for pos in range(0, (str_len-kmer_len)+1):
            #print "Start position", pos
            """ assign the current kmer within shortestk to a variable """
            kmer = shortestk[pos:(pos+kmer_len)]
            kmers.append(kmer)
    """ sort the list of kmers according to length, while making it a unique list. """
    kmers = sorted(set(kmers), key=len)[::-1]
    #print kmers
    
    """ search each kmer in each fasta sequences, in order, until one is found in every sequence.
    As kmers list start with the longest kmer, this should return the longest kmer within seqs. """
    for kmer in kmers:
        #print "KMER", kmer
        kmerfound = True
        for seq in seq_list:
            #print "SEQ", seq
            if kmer not in seq:
                kmerfound = False
                break
        if kmerfound:
            print
            print kmer
            print
            return kmer
        
fastafile = "/home/zhengt/Documents/MyFiles/Python/rosalind/rosalind_lcsm.txt"
sharedmotif(fastafile)
