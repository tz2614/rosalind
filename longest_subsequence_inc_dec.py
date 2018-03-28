#! usr/bin/env python

"""
	Given: A positive integer n<=10000 followed by a permutation pi of length n.

	Return: A longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.

>>> problem(5, [5, 1, 4, 2, 3])
([1, 2, 3], [5, 4, 2])
"""

import sys

def lcs(s, t):
    lengths = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

    for index_s, base_s in enumerate(s):
        for index_t, base_t in enumerate(t):
            if base_s == base_t:
                lengths[index_s+1][index_t+1] = lengths[index_s][index_t] + 1
            else:
                lengths[index_s+1][index_t+1] = \
                    max(lengths[index_s+1][index_t], lengths[index_s][index_t+1])

    result = []
    x, y = len(s), len(t)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert s[x-1] == t[y-1]
            result = [s[x-1]] + result
            x -= 1
            y -= 1

    return result

def longest_subsequence(n, pi):
	
	incr = lcs(pi, sorted(pi))
	#print incr
	decr = lcs(pi, sorted(pi, reverse=True))
	#print decr
	return (incr, decr)

if __name__ == '__main__':
	dataset = open(sys.argv[1]).readlines()
	n, pi = [line.strip() for line in dataset]
	n = int(n)
	#print n
	pi = map(int, pi.split())
	#print pi
	for seq in longest_subsequence(n, pi):
		print ' '.join(map(str, seq))