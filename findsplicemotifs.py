#!usr/bin/python

import sys

def findsplicemotifs(fasta):
    with open (fasta) as fh: 

        names = []
        s = ""
        t = ""
        bases = ["A", "C", "T", "G"]
        pos = []
        count = 0
        # count keeps track of the number of DNA strings 
    
        for line in fh:            
            line = line.strip()
            #strip empty spaces after the line
            
            if line.startswith(">"):
                names.append(line)
                count += 1

            if count == 1:
                if line[0] in bases:
                    s += line
                    # create the cDNA string
            if count == 2:
                if line[0] in bases:
                    t += line
                    # create the splicesite string
        print names
        print s
        print t
        s = list(s)

        for base in t:
            for i, bp in enumerate(s):
                if base == bp and len(pos) < len(t):
                    pos.append(str(i+1))
        return pos

text="rosalind_sseq.txt"
pos= findsplicemotifs(text)
print " ".join(map(str, pos))