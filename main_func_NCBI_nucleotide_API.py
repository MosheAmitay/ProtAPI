from func_NCBI_nucleotide_API import *
A= func_NCBI_nucleotide_API()
#id_rec = A.search(3, " insulin")

#A.fetch_txt(id_rec)
#A.fetch_xml(id_rec)
#record =A.fetch_xml(id_rec)
print A.get_molecule()
print A.get_primary_accession()
print A.get_definition()
print A.get_comment()
print A.get_accession_version()
print A.get_topology()
print A.get_length()
seq = A.get_sequence()
len1 = len(seq)
print len1
#print A.record
#print A.get_dict()
