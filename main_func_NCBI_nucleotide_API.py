from func_NCBI_nucleotide_API import *
A= func_NCBI_nucleotide_API()
id_rec = A.search(3, " insulin")
record =A.fetch_xml(id_rec)
print A.get_molecule(record)
print A.get_comment(record)
