# ProtAPI
this file include learning about records from the data base nucleotide.
include:
searching records and information about them
fetch a record in text format and xml format, and get details about the records- by get function or dictionary.

## all function:

## init 

Initializing an object- its record (by fetching, and if the user want he can do searching before).

### search

searching record from query. choose the first id from the list and return it.



***

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

continue with more examples.
