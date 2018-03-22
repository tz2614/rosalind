#!/user/bin/python

"""
def RNAtoProtein (RNA):

    Utriplet = ["UUU", "UUC", "UUA", "UUG", "UCU", "UCC", "UCA", "UCG", "UAU", "UAC", "UAA", "UAG", "UGU", "UGC", "UGA", "UGG"] 
    Ctriplet = ["CUU", "CUC", "CUA", "CUG", "CCU", "CCC", "CCA", "CCG", "CAU", "CAC", "CAA", "CAG", "CGU", "CGC", "CGA", "CGG"]
    Atriplet = ["AUU", "AUC", "AUA", "AUG", "AUC", "ACC", "ACA", "ACG", "AAU", "AAC", "AAA", "AAG", "AGU", "AGC", "AGA", "AGG"]
    Gtriplet = ["GUU", "GUC", "GUA", "GUG", "GCU", "GCC", "GCA", "GCG", "GAU", "GAC", "GAA", "GAG", "GGU", "GGC", "GGA", "GGG"]
    triplet = Utriplet + Ctriplet + Atriplet + Gtriplet
    print triplet
    for i in range(0, len(RNA), 3):
        target = RNA[i:i+len(triplet[0])]
        assert(len(target) == len(triplet[0]))
        for u in Utriplet:
            if target == Utriplet[u]:
                Utarget = target
                if Utarget == "UU*":
                    if Utarget == "UUU" or "UUC":
                        protein += "F"
                    elif Utarget == "UUA" or "UUG":
                        protein += "L"
                elif Utarget == "UC*":
                    protein += "S"
                elif Utarget == "UA*":
                    if Utarget == "UAU" or "UAC":
                        protein += "Y"
                    else:  
                        break
                elif Utarget == "UG*":
                    if Utarget == "UGU" or "UGC":
                        protein += "C"
                    elif Utarget == "UGG":
                        protein += "W"
                    else:
                        break
                elif target == Ctriplet[i]:
                    Ctarget = target
                    if Ctarget == "CU*":
                        protein += "L"
                    elif Ctarget == "CC*":
                        protein += "P"
                    elif Ctarget == "CA*":
                        if Utarget == "CAU" or "CAC":
                            protein += "H"
                        else:
                            protein += "Q"
                    elif Ctarget == "CG*":
                        protein += "R"
                elif target == Atriplet:
                    Atarget = target
                    if Atarget == "AU*":
                        if Atarget == "AUG":
                            protein += "M"
                        else:
                            protein += "I"
                    elif Atarget == "AC*":
                        protein += "T"
                    elif Atarget == "AA*":
                        if Atarget == "AAU" or "AAC":
                            protein += "N"
                        else:
                            protein += "K"
                    elif Atarget == "AG*":
                        if Utarget == "AGU" or "AGC":
                            protein += "S"
                        else:
                            protein += "R"
                elif target == Gtriplet:
                    Gtarget = target
                    if Gtarget == "GU*":
                        protein += "V"
                    elif Gtarget == "GC*":
                        protein += "A"
                    elif Gtarget == "GA*":
                        if Gtarget == "GAU" or "GAC":
                            protein += "D"
                        else:
                            protein += "E"
                    elif Gtarget == "GG*":
                        protein += "G"
                    else:
                        break
                else:
                    return ""
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

file = open("rosalind_prot.txt", "r")
RNA = file.read()
protein = []
for i in range(0, len(RNA)-3, 3):
    protein.append(RNAdict[RNA[i:i+3]])
protein.remove("Stop")
print "".join(protein)
file.close()

"""print RNAtoProtein(RNA)"""