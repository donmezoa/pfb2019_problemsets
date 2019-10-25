#!/usr/bin/env python3
class DNARecord(object):
  
  # define class attributes
	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name
		self.length = self.get_seq_len()
		self.nt_count = self.nt_comp()
		self.gc_count = self.gc_cont()
		self.fa_format = self.create_fa()

	def get_seq_len(self):
		length = len(self.sequence)
		return length

	def nt_comp(self):
		nt_count = ''
		a_count = str(self.sequence.count('A'))
		t_count = str(self.sequence.count('T'))
		g_count = str(self.sequence.count('G'))
		c_count = str(self.sequence.count('C'))
		nt_count = 'A:' + a_count + ' ' + 'T:' + t_count + ' ' + 'G:' + g_count + ' ' + 'C:' + c_count
		return nt_count

	def gc_cont(self):
		length = len(self.sequence)
		g_count = self.sequence.count('G')
		c_count = self.sequence.count('C')
		gc_count = (g_count + c_count) / length
		return gc_count

	def create_fa(self):
		format_fa = '>' + self.gene_name + ' ' + self.species_name + self.sequence
		return fa_format





dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')

for d in [ dna_rec_obj_1 ]:
	print('name:' , d.gene_name , ' ' , 'seq:' , d.sequence , ' ' , 'length:' , d.length , ' ' , 'species:' , d.species_name)
	print(d.nt_count)
	print('GC content:' , d.gc_count)
	print(d.fa_format)

