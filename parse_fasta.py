#! usr/bin/env python

import sys

def parse_fasta(dataset):
    "Parses data in FASTA format, returning a dictionary of ID's and values"
    records = DefaultOrderedDict(str)
    record_id = None
    for line in [l.strip() for l in dataset.splitlines()]:
        if line.startswith('>'):
            record_id = line[1:]
        else:
            records[record_id] += line
    return records

if __name__ == '__main__':

	dataset = sys.argv[1]
	parse_fasta(dataset)