# YNpdb
A Python Rest_API for the RCSB Protein Data Bank

YNpdb includs one function:

search_pdb()- gets a list of pdb ids and a list of columns(records) of interest 
                 and prints and returns the information about them arranged as a dictionary.
                
## Install
For using my library you must install the libraries: requests, xmltodict, urllib2, json, os
## Examples
### search_pdb()

1.

ids = ['5NUU']

columns = ['taxonomyId']

dict_1 = YNpdb.search_pdb(ids, columns) 

{

    {

     "5NUU: taxonomyId in chain A": "7787"
    
    }

    the results are also saved in output.txt

}

-----------------------------
2.

ids = ['6GUS']

columns = ['chainLength','ligandId']

dict_1 = YNpdb.search_pdb(ids, columns)

{

    {

    "6GUS: chainLength in chain A": "155",
    
    "6GUS: ligandId in chain A": "SO4"
    
    }

    the results are also saved in output.txt
    
}

-----------------------------
3.

ids = ['6EGC']

columns = ['sequence']

dict_1 = YNpdb.search_pdb(ids, columns)

{

    {

    "6EGC: sequence in chain A":         "GSHMTRTEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQQGPPGNEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQD"

    }

    the results are also saved in output.txt

}

------------------------------
4.

ids = ['6DJH','6QN9']

columns = ['compound']

dict_1 = YNpdb.search_pdb(ids, columns)

{

    {

    "6DJH: compound in chain A": "Tyrosyl-DNA phosphodiesterase 1",
    
    "6DJH: compound in chain B": "Tyrosyl-DNA phosphodiesterase 1",
    
    "6QN9: compound in chain H": "Heavy chain",
    
    "6QN9: compound in chain L": "light chain"
    
    }

    the results are also saved in output.txt

}
