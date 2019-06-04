# ProtAPI
This a python 2.7 API for several DataBases-NCBI's geo and nucleotide, RCSB Protein Data Bank (PDB) and Uniprot.
The API uses rest-API for querying and retrieving data.
The API parses the xml based data with Biopython for nucleotide, manually for PDB and Uniprot, and BeautifulSoup4 for geo.

## usage
### geo
the geoParse.py file needs a database name, a file of accessions and a term to search for- wich is one of the sub titles of the GPL accession page. For example, if I want the "Technology type" I will enter the string exactly like it is written in the web-page.
The output will be given in the file output.txt in the order of the accessions accepted in the accessions file.
