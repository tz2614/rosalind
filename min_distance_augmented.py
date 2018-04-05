#! usr/bin/env python

"""
Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).

Return: The edit distance dE(s,t) followed by two augmented strings s' and t' representing an optimal alignment of s and t.
"""

import sys

def parse_fasta(dataset):

    """
    Parses data in FASTA format, returning a dictionary of ID's and values
    """

    records = {}
    record_id = None

    for line in [lines.strip() for lines in dataset.splitlines()]:
        
        if line.startswith('>'):
            records_id = line[1:]
            records[records_id] = ""
        else:
            records[records_id] += line
            #print records
    
    return records

def edit_distance(seq1, seq2):

    # initialise the distance and traceback matrices with zeros.

    distance = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

    traceback = [[0 for index_t in range(len(t)+1)] for index_s in range(len(s)+1)]

    # each pos in the first row and column get (-1) gap penality

    for index_s in range(1, len(s)+1):
        distance[index_s][0] = index_s
    for index_t in range(1, len(t)+1):
        distance[0][index_t] = index_t

    # populate the distance and traceback matrices

    for index_s in range(1, len(s)+1):
        for index_t in range(1, len(t)+1):
            scores = [distance[index_s-1][index_t-1] + (s[index_s-1] != t[index_t-1]), # 0 = match
                      distance[index_s-1][index_t] + 1,                                # 1 = insertion
                      distance[index_s][index_t-1] + 1]                                # 2 = deletion
            distance[index_s][index_t] = min(scores)
            traceback[index_s][index_t] = scores.index(distance[index_s][index_t])

    # fill the edit distance of the last pos in the distance matrix

    edit_dist = distance[-1][-1]

    # initialise aligned strings as variables
    s_align, t_align = s, t

    # traceback to the edge of the matrix starting at the bottom right
    index_s, index_t = len(s), len(t)

    while index_s > 0 and index_t > 0:
        if traceback[index_s][index_t] == 1:
            index_s -= 1
            t_align = t_align[:index_t] + '-' + t_align[index_t:]
        elif traceback[index_s][index_t] == 2:
            index_t -= 1
            s_align = s_align[:index_s] + '-' + s_align[index_s:]
        else:
            index_s -= 1
            index_t -= 1

    # prepend indels if necessary

    for dash in range(index_s):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(index_t):
        s_align = s_align[:0] + '-' + s_align[0:]

    return edit_dist, s_align, t_align


if __name__ == '__main__':

    dataset = open(sys.argv[1]).read()
    dataset = parse_fasta(dataset)
    s, t = dataset.values()
    print ('\n'.join(map(str, edit_distance(s, t))))
