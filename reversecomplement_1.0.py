def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

def complement(Nucleotide):
    if Nucleotide == "A":
        return "T"
    elif Nucleotide == "T":
        return "A"
    elif Nucleotide == "C":
        return "G"
    elif Nucleotide == "G":
        return "C"
    else:
        return ""       

def ReverseComplement(Pattern):
    revComp = [] # output variable
    for x in Pattern:
        revComp.append(x)
    revComp = reverse(revComp)
    revComp = [complement(x) for x in revComp]
    return "".join(revComp)

Pattern = file("rosalind_revc.txt").read()

print ReverseComplement(Pattern)