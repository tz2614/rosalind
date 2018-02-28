import sys

def GCcontent(fasta):
    # create file handle to access the fasta file
    with open (fasta) as fasta_filehandle:
        currentname = ""
        currentseq = ""
        seqs = {}
    # iterate through each line of the file, create a dict with 
    # currentname of seq as key, currentseq of dict as value
        for line in fasta_filehandle:
            line = line.strip()

            if line.startswith(">"):
                if currentname:
                    seqs[currentname] = currentseq

                currentname = line.replace(">", "")  
                currentseq = ""

            else:
                currentseq += line

            seqs[currentname] = currentseq

        # iterate through the seqs and establish the GC ratio of each seq
        GCdict = {}
        for item in seqs.items():
            #print item
            GCcount = 0
            total = 0
            name, seq = item

            for i in seq:

                if i in ["G", "C"]:
                    GCcount += 1
                    total += 1

                else:
                    total += 1

            GCratio = GCcount / float (total) * 100

            GCdict[name] = GCratio
        # iterate through GCdict to find the name with the highest gc content  
        highestgc = -float("inf")
        hgcname = ""

        for item in GCdict.items():
            name, GCratio = item

            if GCratio > highestgc:
                highestgc = GCratio
                hgcname = name

        print hgcname 
        print highestgc

        #alternative solution
        #max(GCratio, key=GCratio.get)

fasta = sys.argv[1]
GCcontent(fasta)

#initial attempt
"""
    DNAdict = {}
    index = []
    DNA = ""
    # count keeps track of the number of DNA strings
    count = 0    
    motif = ""
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            currentseq = line 
        #add the the DNA string as key to dictionary
        else:
            DNA.append(line)
        #create key value pair in dictionary with currentseq as key, and DNA as value.
            DNAdict[currentseq] = DNA
    print DNAdict        
"""
