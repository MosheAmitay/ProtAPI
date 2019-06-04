# YNpdb
A Python Rest_API for the RCSB Protein Data Bank

YNpdb includs two functions:
1. search_pdb()- askes for pdb ids and columns(records) of interest 
                 and prints the information about them arranged.
2. print_all()- askes for pdb ids and columns(records) of interest 
                and prints the full records as a dictionary.
## Install
For using my library you must install the libraries: requests, xmltodict, urllib2, json, os
## Examples
### search_pdb()
---------------------------
Enter the ids that you are interested in (separated by commas): 5NUU

Enter the columns that you are interested in (separated by commas):
 choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: taxonomyId

{

    "5NUU: taxonomyId in chain A": "7787"
    
}


the results are also saved in output.txt

### print_all()
---------------------------

