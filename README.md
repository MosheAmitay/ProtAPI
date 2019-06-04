# ProtAPI
This a python 2.7 API for several DataBases-NCBI's geo and nucleotide, RCSB Protein Data Bank (PDB) and Uniprot.
The API uses rest-API for querying and retrieving data.
The API parses the xml based data with Biopython for nucleotide, manually for PDB and Uniprot, and BeautifulSoup4 for geo.

## usage
### geo
the geoParse.py file needs a database name, a file of accessions and a term to search for- wich is one of the sub titles of the GPL accession page. For example, if I want the "Technology type" I will enter the string exactly like it is written in the web-page.
#### --------------------------------
code example:
python geoParse.py
please enter the database you need:   geo
please enter name of a file with the accessions:   ids5.txt
please enter the field your'e interested in extracting:   Technology type
the results are in output.txt

The accession file is:
GPL10012
GPL10013
GPL10014
GPL10040
GPL10072

The output will be given in the file output.txt in the order of the accessions accepted in the accessions file:
spotted oligonucleotide
spotted oligonucleotide
spotted oligonucleotide
spotted oligonucleotide
spotted oligonucleotide
#### --------------------------------
#### --------------------------------
python geoParse.py
please enter the database you need:   geo
please enter name of a file with the accessions:   ids5.txt
please enter the field your'e interested in extracting:   Title
the results are in output.txt

The accession file is:
GPL10012
GPL10013
GPL10014
GPL10040
GPL10072

The output will be given in the file output.txt in the order of the accessions accepted in the accessions file:
SuperArray Oligo GEArray Mouse Angiogenesis Microarray OMM-024
SuperArray Oligo GEArray Mouse Cancer PathwayFinder Microarray OMM-033
UWBMC Armigeres subalbatus 18K v1.0
Chr. Hansen A/S_Bifidobacterium animalis subsp lactis BB12_1689_v1.0
AGRF Leptospira interrogans spotted oligo array
#### --------------------------------
