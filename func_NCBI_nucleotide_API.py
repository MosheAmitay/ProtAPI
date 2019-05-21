from Bio.PDB.PDBParser import PDBParser
from Bio import Entrez
from Bio import SeqIO
from Bio.PDB import *
import json, os
Entrez.email = "tamarsoyonov@gmail.com"
__metaclass__=type

class func_NCBI_nucleotide_API:
        'This class include function search and xtracting information on record. near to every function there is explanation for using this function.'

        Entrez.email = "tamarsoyonov@gmail.com"


        #searching record from query and print the searching results. print the ids list. choose the first id from the list and return it.
        def search(self, ret_max, term_s):
                handle = Entrez.esearch(db="nucleotide", retmax=ret_max, term=term_s, idtype="acc")
                record = Entrez.read(handle)
                print json.dumps(record,indent=4)
                print record["IdList"]
                id_rec =  record["IdList"][0]
                return id_rec

        #how to use:
        #id_rec = search(3, " insulin")

        #this function get the id of record and print the record at text format.
        def fetch_txt(self, id_rec):
                handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="text")
                print handle.read()

        #how to use:
        #fetch_txt(id_rec)

        # this function fetch a record in xml format, print the record and the keys of the record.
        #return the record.
        def fetch_xml(self, id_rec):
                handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="xml")
                record=Entrez.read(handle)
                record=record[0]
                print "the record: "
                print json.dumps(record,indent=4)
                print "the keys: "
                print(record.keys())
                return record

        #how to use:
        #record =fetch_xml(id_rec)


        def get_sequence(self, record):
                return record["GBSeq_sequence"]

        #how to use:
        #sequence = get_sequence(record)

        def get_molecule(self, record):
                return record["GBSeq_moltype"]

        #how to use:
        #molecule = get_molecule(record)

        def get_comment(self, record):
                return record["GBSeq_comment"]

        #how to use:
        #comment = get_comment(record)


        def get_organism(self, record):
                return record["GBSeq_source"]

        #how to use:
        #organism = get_organism(record)

        def get_primary_accession(self, record):
                return record["GBSeq_primary-accession"]

        #how to use:
        #primary_accession = get_primary_accession(record)

        def get_definition(self, record):
                return record["GBSeq_definition"]

        #how to use:
        #definition = get_definition(record)

        def get_accession_version(self, record):
                return record["GBSeq_accession-version"]

        #how to use:
        #accession_version = get_accession_version(record)

        def get_topology(self, record):
                return record["GBSeq_topology"]

        #how to use:
        #topology = get_topology(record)

        def get_length(self, record):
                return record["GBSeq_length"]

        #how to use:
        #length = get_length(record)

        def get_dict(self, record):
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

        #how to use:
        #dic = get_dict(record)


