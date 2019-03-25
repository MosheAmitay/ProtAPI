#!/usr/bin/env python
from Bio.PDB.PDBParser import PDBParser
from Bio import Entrez
from Bio import SeqIO
from Bio.PDB import *
import json
Entrez.email = "tamarsoyonov@gmail.com"

#seacrh records according to inputs

#handle = Entrez.esearch(db="nucleotide", retmax=1, term="homo sapiens[ORGN] insulin", idtype="acc")
handle = Entrez.esearch(db="nucleotide", retmax=3, term=" insulin", idtype="acc")
record = Entrez.read(handle)

#print the records
print json.dumps(record,indent=4)


#print the ids that return from the search
print record["IdList"]
for i in record["IdList"]:
	print "id record: "+ i 

print "Count: "+ record["Count"]

first_term= record["TranslationStack"][0]['Term']
print first_term

#print the TranslationStack
print " TranslationStack" + json.dumps(record["TranslationStack"],indent=4)

handle.close()


#fetch a record in text format
#the id from NCBI you want to fetch enter string of id
id_rec = record["IdList"][0]
handle2 = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="text")
print handle2.read()

handle2.close()
exit()

handle3 = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="xml")
print "handle3: " 
print  handle3.read() 

#have a problem
#record3=  Entrez.read(handle3)
#print len(record3)
#print(record3[0].keys())
#print record3[0]["GBSeq_strandedness"]
handle3.close()

#here we want to search the pdb for insulin and download the file by pyPDB

parser = PDBParser()
structure = parser.get_structure('5IEI','5IEI.pdb')
header = structure.header
#print header.keys()
#print "name ", header["name"]
#print "journal ", header["journal"]
print "compound" , header["compound"]["1"]["chain"]

#wget https://www.ncbi.nlm.nih.gov/protein/P13569.3
