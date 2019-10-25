#!/usr/bin/env python3

import os, sys, re

sam_filename = sys.argv[1]

reads_set = set()

sam_dict = {}

sam = open(sam_filename)
for line in sam:
	line = line.rstrip()
	line = line.split('\t')
	gene = line[2]
	gene = gene.split('^')
	gene = gene[0]
	reads_set.add(line[0])
	sam_dict[gene] = reads_set

for gene in sam_dict:
	print(gene)



#print(reads_set)
#print(sam_dict)



# 


