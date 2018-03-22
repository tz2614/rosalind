#! usr/bin/env python

    """
    Given two strings s and t of equal length, the Hamming distance between s
    and t, denoted HammingDistance(s,t), is the number of corresponding symbols that differ
    in s and t. See Figure 2.

    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

    Return: The Hamming distance HammingDistance(s,t).
    """

def HammingDistance(s, t):
#    s = s.upper()
#    s = list(s)
#    t = t.upper()
#    t = list(t)
#    s = list(map(int, s()))
#    t = list(map(int, t()))
    dist = 0
    for i in range(len(p)):
        if s[i] != t[i]:
            dist += 1
    return dist

s = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
t = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
print HammingDistance(p, q)