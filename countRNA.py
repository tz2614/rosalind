#!user/bin/python

import string

DNA = file('rosalind_rna.txt').read()
RNA = string.replace(str(DNA), 'T', "U")
print RNA
