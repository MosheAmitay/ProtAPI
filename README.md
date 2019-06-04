# Prot API

## Uniprot

UniProt is a freely accessible database of protein sequence and functional information, many entries being derived from genome sequencing projects. It contains a large amount of information about the biological function of proteins derived from the research literature.  
https://en.wikipedia.org/wiki/UniProt.

Since this is a very large data base, access of information can be a burden especially when information of more than one accession number is wanted.

## Description
This is a class meant to help users retrieve specific data for 1 or more accession numbers.
This class is made up of 8 definitions:

1.	GeneName: finds gene name/s of given accession number/s.
2.	Title: finds title of accession number/s.
3.	ProteinName: finds the protein name/s of given accession number/s.
4.	Organism: finds name/s of organism/s of given accession number/s.
5.	ProteinSeq: finds the protein sequence/s of given accession number/s.
6.	Modified: finds modified genes in given accession number/s.
7.	Variations: finds variations for given accession number/s.
8.	PrintAll: prints all the data at once for all the accession numbers given.

## How To Use
1.	Create a youreName.py file
2.	Include the following import:
from UniprotApi import *
3.	Create a variable for the UniprotApi class:
youreName = UniprotApi()
4.	Use the variable to call one or all of the functions mentioned in the description:
youreName.GeneName()
youreName.Title()
youreName.ProteinName()
youreName.Organism()
youreName.ProteinSeq()
youreName.Modified()
youreName.Variations()
youreName.PrintAll()

## Code Examples:
Once you have youreName.py file created (mentioned in the 'how to use section')

1. To extract gene names:

youreName.py file will include:

from UniprotApi import *

VarName = UniprotApi()

VarName.GeneName()

you will run youreName.py in the linux window:

python youreName.py

Please Enter Accession Numbers (seperated by spaces): Q14533 Q3TTY5 P08069 Q60751 P69892

(the results you will get:)

Gene Name Of Q14533: KRT81

Gene Name Of Q3TTY5: Krt2

Gene Name of P08069: IGF1R

Gene Name of Q60751: Igf1r

Gene Name of P69892: HBG2

2. To extract protein names for all the accession numbers:

youreName.py will include:

from UniprotApi import *

VarName = UniprotApi()

VarName.ProteinName()

you will run youreName.py in the linux window:

python youreName.py

Please Enter Accession Numbers (seperated by spaces): Q14533 Q3TTY5 P08069 Q60751 P69892

(the results you will get:)

Protein Name Of Q14533: Keratin, type II cuticular Hb1

Protein Name Of Q3TTY5: Keratin, type II cytoskeletal 2 epidermal

Protein Name Of P08069: Insulin-like growth factor 1 receptor

Protein Name Of Q60751: Insulin-like growth factor 1 receptor

Protein Name Of P69892: Hemoglobin subunit gamma-2










