from Bio.PDB.PDBParser import PDBParser
from Bio import Entrez
from Bio import SeqIO
from Bio.PDB import *
import json
Entrez.email = "tamarsoyonov@gmail.com"
handle3 = Entrez.efetch(db="nucleotide", id='M38195', rettype="gb", retmode="xml")
record3=Entrez.read(handle3)
record3=record3[0]
print  json.dumps(record3,indent=4)
