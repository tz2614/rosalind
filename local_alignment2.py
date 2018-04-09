#! usr/bin/env python

"""
Problem: Local Alignment with Scoring Matrix
URL: http://rosalind.info/problems/loca/

Given: Two protein strings s and t in FASTA format (each having length at most
1000 aa).

Return: A maximum alignment score along with substrings r and u of s and t,
respectively, which produce this maximum alignment score (multiple solutions may
exist, in which case you may output any one). Use:
    - The PAM250 scoring matrix.
    - Linear gap penalty equal to 5.

EXAMPLE INPUT:
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

EXAMPLE OUTPUT:
(note: this is correct, but different than Rosalind sample output):
23
MEANLYPRTEINSTRIN
LEASANTLYEINSTEIN

"""

def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = {}
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
            records[record_id] = ""
        else:
            records[record_id] += line
    return records

def local_alignment(v, w, scoring_matrix, sigma):
    '''Returns the score and local alignment with the given scoring matrix and indel penalty sigma for strings v, w.'''
    from numpy import unravel_index, zeros

    # Initialize the matrices.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], 0]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell in the matrix and the high score.
    i,j = unravel_index(S.argmax(), S.shape)
    max_score = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
        elif backtrack[i][j] == 1:
            j -= 1
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned