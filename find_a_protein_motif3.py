#! usr/bin/env python

import fasta
import urllib2
import re
import sys

def read_dataset(filename):
	proteins = []
	f = open(filename, 'r')
	for line in f:
		if len(line) > 0:
			proteins.append(line.lstrip().rstrip())
	return proteins

def convert_motif_to_regex(motif):
	re_string = "(?=" + motif.replace("{", "[^").replace("}", "]") + ")"
	return re.compile(re_string)

base_url = "http://www.uniprot.org/uniprot/"
dataset = sys.argv[1]
proteins = read_dataset(dataset)
motif = "N{P}[ST]{P}"
motif_regex = convert_motif_to_regex(motif)

for p in proteins:
	url = base_url + p + ".fasta"
	lines = []
	file_content = urllib2.urlopen(url)
	for line in file_content:
		lines.append(line)
	reader = fasta.FastaReader.fromlines(lines)
	matching_locs = []
	for record in reader.records:
		for match in re.finditer(motif_regex, record.dna):
			matching_locs.append(str(match.start() + 1))
	if len(matching_locs) > 0:
		print p, "\n", " ".join(matching_locs)