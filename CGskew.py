def Skew(Genome):
    count = 0
    positions = 0
    nucleotides = {0:0} #initializing the dictionary
    for i in Genome:
        positions += 1
        if i == "C":
            count -= 1
        if i == "G":
            count += 1
        nucleotides[positions] = count
    return nucleotides

Genome = "GATACACTTCCCGAGTAGGTACTG"
print Skew(Genome)

def MaximumSkew(Genome):
    index = [] # output variable
    bestscore = None
    scores = Skew(Genome)
    for position, score in scores.items():
        if bestscore is None:
            bestscore = score
        if score > bestscore:
            bestscore = score
            index = []
            index.append(position)
        elif score == bestscore:
            index.append(position)
        else:
            pass       
    return index

print MaximumSkew(Genome)