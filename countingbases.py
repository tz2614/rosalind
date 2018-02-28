#!user/bin/python

def DNAcount(string):
    A = 0
    C = 0
    T = 0
    G = 0
    X = 0
    bases = ["A", "C", "G", "T"]
    for i in range(len(string)):
        if string[i] == bases[0]:
            A += 1
        elif string[i] == bases[1]:
            C += 1
        elif string[i] == bases[2]:
            G += 1
        elif string[i] == bases[3]:
            T += 1
        else:
            X += 1
    count = [str(A), str(C), str(G), str(T)]
    print (" ".join(count))

string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
DNAcount(string)