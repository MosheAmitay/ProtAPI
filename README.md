# ProtAPI
this file include learning about records from the data base nucleotide.
include:
searching records and information about them
fetch a record in text format and xml format, and get details about the records- by get function or dictionary.

## all function:

### init 

Initializing an object- its record (by fetching, and if the user want he can do searching before).

### search

searching record from query. choose the first id from the list and return it.

### search_and_print

searching record from query and print the searching results. print the ids list. choose the first id from the list and return it.

### fetch_txt

this function get the id of record and print the record at text format.

### fetch_xml

this function fetch a record in xml format and return the record.

### fetch_and_print_xml

this function fetch a record in xml format, print the record and the keys of the record. return the record.

### get_sequence

This function return the sequence of object.

### get_molecule

This function return the kind of the molecule of the object.

### get_comment

This function return a comment on the record of the object.

### get_organism

This function return the organism of object.

### get_primary_accession

This function return the accession on the record of the object.

### get_definition

This function return a definition on the record of the object.

### get_accession_version

This function return the accession version on the record of the object.

### get_topology

This function return the topology of object.

### get_length

This function return the length of the sequence of object.

### get_dict

Function that return dictionary with data on the object.

## Install
For using my class you must install: 

from Bio.PDB.PDBParser import PDBParser

from Bio import Entrez

from Bio import SeqIO

from Bio.PDB import *

import json, os

## How to use
1. you need to create python file (for example: main_func_NCBI_nucleotide_API.py)

2. you need to install my class: from func_NCBI_nucleotide_API import *

3. you need to create an object, for example: A = func_NCBI_nucleotide_API() 

4. you need to choose if you want to search term. if yes- write your maximum record you want and the term, if no- write your id record.

5. then, you can extract information by get functions

6. you can also use search and fetch function with or without printing.

## Examples
---------------------------------

the function: get_molecule()

---------------------------------

you need to write at your file: print A.get_molecule()

then: python main_func_NCBI_nucleotide_API.py

you get:

Do you want to search? (y/n):    y

Write your ret_max:    4

Write your term:    cftr

mRNA

--------------------------------

the function: get_sequence()

--------------------------------

you need to write at your file: print A.get_sequence()

then: python main_func_NCBI_nucleotide_API.py

you get:

Do you want to search? (y/n):    y

Write your ret_max:    2

Write your term:    mus musculus

gtgagtacttggaaaggactcggaaagatgcatctagtcttgctgatctgcctgctggcaggaaccactgggaagagctgcctccgctgctggccagagctgctcgccatgatggactatgacctgcaggtgctctggggcagtccagggccacctacagaactctcacaaagcctacactcctttttcctggagaataacaccatattcttgccctggtatcttgctcgagacaatttggatgaggaaacagctacatttttcacccaagtagacaacgccattaaaaagctgagggatgataagccagcactgcttaatgagattcgggttcagaagagtctcctggacgagaggctgaaggagaagtcccaggacctgatgcagaaggtctgcaatgagtcctgtgacatcctctccgaaatggaagtcactgcatgtgctgactgccggaagttctacctgtcctgcaatgactctaccttgtgcacagccagggtcacatggagctacaagtgggttgtagtccttttcaccatcttgatgttcctggctgttgctggcattggtggatactttttctggctccagaagaggtcagcggaggctgataagagaagagacagcaagttacttccttcaggaaacgaccagcaactagggcagcaaccagagcagctgccagagcccatgctgtctgaaagctgtctctggccctggtgactctctattgcacaaagcactccttcctgggacctggagagctctgaggccctgcagctctgcagacaagactgatatattctctctctctctctctctctctccctccctccctccctccctcccttcctccctccctccctcctaatacatactcctttgtaaatagttattaaaaacatttttcctatata

--------------------------------

the function: 

--------------------------------
