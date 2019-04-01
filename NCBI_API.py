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
print "id rec: "
handle2 = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="text")
#print handle2.read()

handle2.close()

dict_NCBI=dict()


#fetch a record in xml format
#the id from NCBI you want to fetch enter string of id
handle3 = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="xml")
print "handle3: "

record3=Entrez.read(handle3)
record3=record3[0]
print  json.dumps(record3,indent=4)


#print details about the record
print len(record3)
print(record3.keys())
print "strandedness: " +  record3["GBSeq_strandedness"]
print "sequence: " + record3["GBSeq_sequence"]
print "molecule type: " + record3["GBSeq_moltype"]

#create heavy dictionary to record of the NCBI
dict_NCBI["strandedness"]=record3["GBSeq_strandedness"]
dict_NCBI["sequence"]=record3["GBSeq_sequence"]
dict_NCBI["molecule type"]=record3["GBSeq_moltype"]
dict_NCBI["organism"]=record3["GBSeq_source"]
dict_NCBI["primary-accession"]=record3["GBSeq_primary-accession"]
dict_NCBI["definition"]=record3["GBSeq_definition"]
dict_NCBI["accession-version"]=record3["GBSeq_accession-version"]
dict_NCBI["topology"]=record3["GBSeq_topology"]
dict_NCBI["length"]=record3["GBSeq_length"]
#dict_NCBI[""]=record3["GBSeq_feature-table"] #here. need to check on another record.



print "dict_NCBI: "
print dict_NCBI

handle3.close()

#def basic_data_by_id(entry_id):

#       handle3 = Entrez.efetch(db="nucleotide", id=entry_id, retmode="xml")
#       print "gv"

