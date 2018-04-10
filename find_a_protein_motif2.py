#! usr/bin/env python

import re
import requests
import sys

REQUEST_URL = "http://www.uniprot.org/uniprot/{}.fasta"
GLYC_REGEX = re.compile(r"(?=(N[^P][ST][^P]))")


def find_glycosylation_motif(uniprot_id):
    r = requests.get(REQUEST_URL.format(uniprot_id))
    seq = "".join(r.text.split('\n')[1:])
    return [m.start() + 1 for m in GLYC_REGEX.finditer(seq)]


def process_uniprots(uniprot_ids):
    for up_id in uniprot_ids:
        motifs = [str(m) for m in find_glycosylation_motif(up_id)]
        if motifs:
            print(up_id)
            print(" ".join(motifs))

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        process_uniprots(f.read().strip().split('\n'))


