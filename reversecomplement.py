#!usr/bin/python
#
#
#
#
#
# Tengyue Zheng (28 Feb 2018) contact: tony_zheng35@hotmail.com

"""
The aim of the function is to produce a reverse complement copy of the 
DNA string provided.  

To run the script, make sure that Python 2.0 or later is installed in your 
system. If you have Python 3.6 or later installed, then please change the
print statements in the script, so that the output of the functions can be displayed properly.

Note:

<<>> - This means that replace the content with appropriate text string

Instructions:

navigate to the directory where the script is stored.

directory path = ~/Documents/MyFiles/Python/rosalind$ 

At the command prompt
e.g. user@user: 

type the following

python reversecomplement.py <<DNA string>>
"""

import sys

def reverse(DNA):

    """Create a DNA string in reverse order using argument provided as input

        Args:
        DNA (str): DNA string to reverse

        Returns:
        reverse sequence of DNA string"""

    revseq = ""
    l = len(DNA) - 1
    while l >= 0:
        revseq = revseq + DNA[l]
        l -= 1
    return revseq

def complement(Nucleotide):

    """create a complement sequence of the DNA string provided

        Args:
        Nucleotide (str): DNA string to complement

        Returns:
        complement sequence of DNA string"""

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

def ReverseComplement(DNA):

    """Using previous two functions, create a reverse complement of the DNA string.
    
        Args:
        DNA (str): DNA string to reverse and complement

        Returns:
        reverse complement sequence of the DNA string in a print statement
    """

    bases = ["A", "C", "T", "G"]

    # if individual bases in the DNA string does not match A C T or G, then an error message is displayed on terminal. 
    basecheck = [(i, x) for i, x in enumerate(DNA) if x not in bases]
    
     # The position of the inapproriate base is displayed as a number in the error message.
    assert not basecheck, basecheck

    # calling previous two functions to reverse and complement the sequence
    revcompseq = [complement(x) for x in reverse(DNA)]
    # make the reverse complement sequence output into a string
    revcompseq = "".join(revcompseq)

    return "Here is the reverse complement sequence: {}".format(revcompseq)

def main(seq):

    """this function ensures that when the script is executed on command line, the 
    ReverseComplement function is called"""

    revcompseq = ReverseComplement(seq)
    print revcompseq

if __name__ == "__main__":
    
    """this enable the user to enter a DNA string as an argument on the command line, 
    as an input to the command function"""

    main(sys.argv[1])

# seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
