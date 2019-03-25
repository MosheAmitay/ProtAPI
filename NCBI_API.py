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
#print handle2.read()

handle2.close()

#fetch a record in xml format
#the id from NCBI you want to fetch enter string of id
handle3 = Entrez.efetch(db="nucleotide", id=id_rec, retmode="xml")
print "handle3: " 
print  handle3.read() 

record3=  Entrez.read(handle3)
record3=record3[0]
#print details about the record
print json.dumps(record3,indent = 4)
print len(record3)
print(record3.keys())
print "strandedness: " +  record3["GBSeq_strandedness"]
print "sequence: " + record3["GBSeq_sequence"]
print "molecule type: " + record3["GBSeq_moltype"]
handle3.close()
