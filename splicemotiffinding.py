import sys

def findmotif(fasta):
    with open (fasta) as fasta_filehandle: 

        DNA = ""
        motif = ""
        positions = []
        # count keeps track of the number of DNA strings
        count = 0    
    
        for line in fasta_filehandle:
            line = line.strip()
            
            if line.startswith(">"):
                count += 1
                continue  
            # create the DNA string
            elif count == 1:
                DNA += line
            # create the intron string
            elif count > 1:
                motif += line

        DNA = list(DNA)
        motif = list(motif)
        count = 0
        pos = 0

        for j, motifbase in enumerate (motif):

            for i, DNAbase in enumerate(DNA[pos+1:]):

                if motif[j] == DNA[i]:
                    pos = i
                    count += 1
                    positions.append(pos+1)

                if count == len(motif):
                    print "count: ", count
                    print "length of motif: ", len(motif)
                    break 
                    return positions

fasta = sys.argv[1]
print findmotif(fasta)