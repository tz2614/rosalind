
def PatternMatching(text):
    #print "hello"
    f = open(text, "r")
    s = f.readline().strip()
    #print len(s)
    t = f.readline().strip()
    #print len(t)
    positions = [] # output variable
    for i in range(len(s)-len(t)+1):
        #print i
        #print s[i:i+len(t)-1]
        #print t
        if s[i:i+len(t)] == t:
            positions.append(i+1)
            #print positions
    return positions

text="rosalind_subs.txt"
patterns = PatternMatching(text)

print " ".join(map(str, patterns))