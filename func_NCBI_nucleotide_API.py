from Bio.PDB.PDBParser import PDBParser
from Bio import Entrez
from Bio import SeqIO
from Bio.PDB import *
import json, os

Entrez.email = "tamarsoyonov@gmail.com"

#function of searching and printing information about the records, return the id record.
def search(ret_max, term_s):
        handle = Entrez.esearch(db="nucleotide", retmax=ret_max, term=term_s, idtype="acc")
        record = Entrez.read(handle)
        print json.dumps(record,indent=4)
        print record["IdList"]
        for i in record["IdList"]:
                print "id record: "+ i

        print "Count: "+ record["Count"]
        id_rec =  record["IdList"][0]
        return id_rec

id_rec = search(3, " insulin")

#this function get the id of record and print the record at text format.
def fetch_txt(id_rec):
        handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="text")
        print handle.read()

fetch_txt(id_rec)

# this function fetch a record in xml format, print the record, its length and the keys of the record.
#return the record.
def fetch_xml(id_rec):
        handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="xml")
        record=Entrez.read(handle)
        record=record[0]
        print "the record: "
        print json.dumps(record,indent=4)
        print "the length: "
        print len(record)
        print "the keys: "
        print(record.keys())
        return record

record =fetch_xml(id_rec)

def get_sequence(record):
        return record["GBSeq_sequence"]

sequence = get_sequence(record)

def get_molecule(record):
        return record["GBSeq_moltype"]

molecule = get_molecule(record)

def get_organism(record):
        return record["GBSeq_source"]

organism = get_organism(record)

def get_primary_accession(record):
        return record["GBSeq_primary-accession"]

primary_accession = get_primary_accession(record)

def get_definition(record):
        return record["GBSeq_definition"]

definition = get_definition(record)

def get_accession_version(record):
        return record["GBSeq_accession-version"]

accession_version = get_accession_version(record)

def get_topology(record):
        return record["GBSeq_topology"]

topology = get_topology(record)

def get_length(record):
        return record["GBSeq_length"]

length = get_length(record)

def get_dict(record):
        dict_NCBI=dict()
        dict_NCBI["sequence"]=record["GBSeq_sequence"]
        dict_NCBI["molecule type"]=record["GBSeq_moltype"]
        dict_NCBI["organism"]=record["GBSeq_source"]
        dict_NCBI["primary-accession"]=record["GBSeq_primary-accession"]
        dict_NCBI["definition"]=record["GBSeq_definition"]
        dict_NCBI["accession-version"]=record["GBSeq_accession-version"]
        dict_NCBI["topology"]=record["GBSeq_topology"]
        dict_NCBI["length"]=record["GBSeq_length"]
        list_for=[]
        for i in record["GBSeq_feature-table"][0]["GBFeature_quals"]:
                key=i["GBQualifier_name"]
                dict_NCBI[key]=i["GBQualifier_value"]

        return dict_NCBI


dic = get_dict(record)

