#!/usr/bin/env python3

from Bio import SeqIO

length = []




for seq_record in SeqIO.parse("ecoli_0.25.contigs.fasta" , "fasta"):
	length_no_sort = '{}'.format(len(seq_record))
	length.append(length_no_sort)


length = length.sort()
print(length)



#	print('ID',seq_record.id)
#	print('Sequence',seq_record.seq)
#	print('Length',len(seq_record.seq))











