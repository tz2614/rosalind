#! usr/bin/env python

"""
    Given: Two permutations mu and gamma, each of length 10.

    Return: The reversal distance drev(mu,gamma), followed by a collection of reversals sorting mu into gamma.
    If multiple collections of such reversals exist, you may return any one

>>> input 
    1 2 3 4 5 6 7 8 9 10
    1 8 9 3 2 7 6 5 4 10

    output
    2
    4 9
    2 5
"""

import collections
import sys

def get_all_permutations(s):
    for i in xrange(len(s)):
        for j in xrange(i + 2, len(s) + 1):
            yield (s[:i] + s[i:j][::-1] + s[j:], (i + 1, j))

def get_reversal_distance(p1, p2):
    if p1 == p2:
        return 0
    
    target = tuple(p2)
    first = {tuple(p1): 0}
    first_histories = {tuple(p1): ()}
    q = collections.deque((p1, ))
    
    while len(q):
        s = q.popleft()
        history = first_histories[s]
        
        for (j, zz) in get_all_permutations(s):
            if j == target:
                return (first[s] + 1, history + (zz, ))
            if not j in first:
                first[j] = first[s] + 1
                first_histories[j] = history + (zz, )
                
                if first[s] != 4:
                    q.append(j)
                    
    second = {tuple(p2): 0}
    second_histories = {tuple(p2): ()}
    target = tuple(p1)
    q = collections.deque((p2, ))
    answer = 100000
    answer_history = ()
    
    while len(q):
        s = q.popleft()
        history = second_histories[s]
        
        for (j, zz) in get_all_permutations(s):
            if not j in second:
                second[j] = second[s] + 1
                second_histories[j] = history + (zz, )
                
                if second[s] != 3:
                    q.append(j)
                    
            if j in first:
                if answer > first[j] + second[j]:
                    answer = first[j] + second[j]
                    answer_history = first_histories[j] + second_histories[j][::-1]
                    
    return answer, answer_history

if __name__ == '__main__':
        
    with open(sys.argv[1]) as f:
        s = tuple(map(int, f.readline().split()))
        t = tuple(map(int, f.readline().split()))
        
        distance, reversals = get_reversal_distance(s, t)
        
        print distance
        
        for (x, y) in reversals:
            print x, y