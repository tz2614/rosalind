#! usr/bin/env python

import collections
import sys

def get_all_permutations(s):
    for i in xrange(len(s)):
        for j in xrange(i+2, len(s)+1):
            yield s[:i] + s[i:j][::-1] + s[j:]

def get_reversal_distance(p1, p2):
    if p1 == p2:
        return 0
    
    target = tuple(p2)
    #print target
    fromfirst = {tuple(p1): 0}
    #print fromfirst
    q = collections.deque((p1, ))
    #print q
    
    while len(q):
        s = q.popleft()
        #print s
        
        for j in get_all_permutations(s):
            if j == target:
                return fromfirst[s] + 1
            
            if not j in fromfirst:
                fromfirst[j] = fromfirst[s] + 1
                
                if fromfirst[s] != 4:
                    q.append(j)
    #print q
    fromsecond = {tuple(p2): 0}
    #print fromsecond
    target = tuple(p1)
    #print target
    q = collections.deque((p2, ))
    #print q
    answer = 100000
    
    while len(q):
        s = q.popleft()
        
        if fromsecond[s] == 4:
            break
        
        for j in get_all_permutations(s):
            if j == target:
                return fromsecond[s] + 1
            
            if not j in fromsecond:
                fromsecond[j] = fromsecond[s] + 1
                
                if fromsecond[s] != 3:
                    q.append(j)
                    
            if j in fromfirst:
                answer = min(answer, fromfirst[j] + fromsecond[j])
        #print q   
    return answer

if __name__ == "__main__":
    distances = []
    
    with open(sys.argv[1]) as s:
        dataset = map(str.strip, s.readlines())
    
    for i in xrange(0, len(dataset), 3):
        s = tuple(map(int, dataset[i].split()))
        t = tuple(map(int, dataset[i + 1].split()))
        
        distances.append(get_reversal_distance(t, s))
        
    print ' '.join(map(str, distances))