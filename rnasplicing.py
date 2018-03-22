#!usr/bin/python
"""
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

Pattern = "AAAATTTT"
Genome = "AAAATTTTAAAATTTTCTAGTACTAGTGCTGATCG"

#print PatternMatching(Pattern, Genome)
"""

RNAdict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",} 

def RNAsplicing(fasta):
    f = open(fasta, "r")
    DNA = ""
    introns = []
    # count keeps track of the number of DNA strings
    count = 0    
    protein = []

    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            count += 1
            continue  
        #create the DNA string
        elif count == 1:
            DNA += line
        #create the intron string
        elif count > 1:
            introns.append(line)
    #print "DNA", DNA
    l = len(DNA)
    n = len(introns)

    for intron in introns:
        DNA = DNA.replace(intron, "")
    #print "DNA", DNA
    
    for base in DNA:
        if base == "T":
            RNA = DNA.replace("T", "U")
    print RNA

    for i in range(0, len(RNA)-3, 3):
        protein.append(RNAdict[RNA[i:i+3]])
        if protein[-1] == "Stop":
            break
    #protein.remove("Stop")
    protein = "".join(protein)
    return protein

#fasta = "rosalind_splc.txt"
#print RNAsplicing(fasta)

    #RNAseq = enumerate(RNAseq)
    #for index, bases in RNAseq:
        #if PatternMatching(intron, RNAseq):
            #RNAseq.remove()
