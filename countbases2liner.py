
nucleotides = file('rosalind_dna.txt').read()
print " ".join([str(nucleotides.count(c)) for c in 'ACGT'])