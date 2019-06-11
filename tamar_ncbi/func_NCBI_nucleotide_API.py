#func_NCBI_nucleotide_API: A class, Python Rest_API for database Nucleotide in NCBI.
#Written by Tamar Bash, 2019.
#Bioinformatics, Jerusalem College of Technology (JCT) Tal-Campus, 2019.

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

        #---------------
        #init function.
        #---------------

        #Initializing an object- its record (by fetching, and if the user want he can do searching before).
        def __init__(self):
                answer_search = raw_input("Do you want to search? (y/n):    ")
                if answer_search == "y":
                        a_ret_max = raw_input("Write your ret_max:    ")
                        a_term_s = raw_input("Write your term:    ")
                        self.id_rec = self.search(a_ret_max, a_term_s)
                        self.record =  self.fetch_xml(self.id_rec)
                if answer_search =="n": #for who want just to fetch.
                        user_id_rec = raw_input("Write your id record:    ")
                        self.record =  self.fetch_xml(user_id_rec)


        #------------------
        #search functions:
        #------------------

        #searching record from query. choose the first id from the list and return it.
        def search(self, ret_max, term_s):
                handle = Entrez.esearch(db="nucleotide", retmax=ret_max, term=term_s, idtype="acc")
                record = Entrez.read(handle)
                id_rec =  record["IdList"][0]
                return id_rec


        #searching record from query and print the searching results. print the ids list. choose the first id from the list and return it.
        def search_and_print(self, ret_max, term_s):
                handle = Entrez.esearch(db="nucleotide", retmax=ret_max, term=term_s, idtype="acc")
                record = Entrez.read(handle)
                print json.dumps(record,indent=4)
                print record["IdList"]
                id_rec =  record["IdList"][0]
                return id_rec

        #------------------
        #fetch functions:
        #------------------

        #this function get the id of record and print the record at text format.
        def fetch_txt(self, id_rec):
                handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="text")
                print handle.read()


        # this function fetch a record in xml format and return the record.
        def fetch_xml(self, id_rec):
                handle = Entrez.efetch(db="nucleotide", id=id_rec, rettype="gb", retmode="xml")
                record=Entrez.read(handle)
                record=record[0]
                return record


        # this function fetch a record in xml format, print the record and the keys of the record.
        #return the record.
        def fetch_and_print_xml(self, id_rec):
                record = self.fetch_xml(id_rec)
                print "the record: "
                print json.dumps(record,indent=4)
                print "the keys: "
                print(record.keys())
                return record



        # =============================================
        #Functions for extract specific information
        # =============================================


        #This function return the sequence of object.
        def get_sequence(self):
                return self.record["GBSeq_sequence"]

        #This function return the kind of the molecule of the object.
        def get_molecule(self):
                return self.record["GBSeq_moltype"]

        #This function return a comment on the record of the object.
        def get_comment(self):
                return self.record["GBSeq_comment"]

        #This function return the organism of object.
        def get_organism(self):
                return self.record["GBSeq_source"]

        #This function return the accession on the record of the object.
        def get_primary_accession(self):
                return self.record["GBSeq_primary-accession"]

        #This function return a definition on the record of the object.
        def get_definition(self):
                return self.record["GBSeq_definition"]

        #This function return the accession version on the record of the object.
        def get_accession_version(self):
                return self.record["GBSeq_accession-version"]

        #This function return the topology of object.
        def get_topology(self):
                return self.record["GBSeq_topology"]

        #This function return the length of the sequence of object.
        def get_length(self):
                return self.record["GBSeq_length"]

        #============================================================
        #Function that return dictionary with data on the object.
        #============================================================

        def get_dict(self):
                dict_NCBI=dict()
                dict_NCBI["sequence"]=self.record["GBSeq_sequence"]
                dict_NCBI["molecule type"]=self.record["GBSeq_moltype"]
                dict_NCBI["organism"]=self.record["GBSeq_source"]
                dict_NCBI["primary-accession"]=self.record["GBSeq_primary-accession"]
                dict_NCBI["definition"]=self.record["GBSeq_definition"]
                dict_NCBI["accession-version"]=self.record["GBSeq_accession-version"]
                dict_NCBI["topology"]=self.record["GBSeq_topology"]
                dict_NCBI["length"]=self.record["GBSeq_length"]
                list_for=[]
                for i in self.record["GBSeq_feature-table"][0]["GBFeature_quals"]:
                        key=i["GBQualifier_name"]
                        dict_NCBI[key]=i["GBQualifier_value"]
                return dict_NCBI
