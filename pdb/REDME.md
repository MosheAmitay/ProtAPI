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

ids = ['6QN9']
columns = ['compound','ligandId']
dict = YNpdb.search_pdb(ids, columns)

{

    {

    "6QN9: compound 1 in chain H": "Heavy chain",
    
    "6QN9: compound 1 in chain L": "light chain",
    
    "6QN9: ligandId 1 in chain H": "null",
    
    "6QN9: ligandId 1 in chain L": "GOL",
    
    "6QN9: ligandId 2 in chain L": "SO4"
    
    }

    the results are also saved in output.txt
    
}
-----------------------------
2.

ids = ['6GUS']

columns = ['chainLength','ligandId']

dict = YNpdb.search_pdb(ids, columns)
{

     {

     "6GUS: chainLength 1 in chain A": "155",
    
     "6GUS: ligandId 1 in chain A": "CL",
    
     "6GUS: ligandId 2 in chain A": "GOL",
    
     "6GUS: ligandId 3 in chain A": "SO4"
    
     }

     the results are also saved in output.txt

}

-----------------------------
3.

ids = ['6EGC']

columns = ['sequence']

dict = YNpdb.search_pdb(ids, columns)

{

    {

    "6EGC: sequence 1 in chain A":         "GSHMTRTEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQQGPPGNEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQD"

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

    "6DJH: compound 1 in chain A": "Tyrosyl-DNA phosphodiesterase 1",
    
    "6DJH: compound 1 in chain B": "Tyrosyl-DNA phosphodiesterase 1",
    
    "6QN9: compound 1 in chain H": "Heavy chain",
    
    "6QN9: compound 1 in chain L": "light chain"
    
    }

    the results are also saved in output.txt

}

-----------------------------------------------
5.

ids = ['6NR9']

columns = ['chainLength']

dict = YNpdb.search_pdb(ids, columns)

{

    {

    "6NR9: chainLength 1 in chain 1": "107",
    
    "6NR9: chainLength 1 in chain 2": "103",
    
    "6NR9: chainLength 1 in chain 3": "132",
    
    "6NR9: chainLength 1 in chain 4": "104",
    
    "6NR9: chainLength 1 in chain 5": "127",
    
    "6NR9: chainLength 1 in chain 6": "102",
    
    "6NR9: chainLength 1 in chain A": "534",
    
    "6NR9: chainLength 1 in chain B": "509",
    
    "6NR9: chainLength 1 in chain C": "513",
    
    "6NR9: chainLength 1 in chain D": "514",
    
    "6NR9: chainLength 1 in chain E": "517",
    
    "6NR9: chainLength 1 in chain F": "515",
    
    "6NR9: chainLength 1 in chain G": "514",
    
    "6NR9: chainLength 1 in chain H": "514",
    
    "6NR9: chainLength 1 in chain I": "534",
    
    "6NR9: chainLength 1 in chain J": "509",
    
    "6NR9: chainLength 1 in chain K": "513",
    
    "6NR9: chainLength 1 in chain L": "514",
    
    "6NR9: chainLength 1 in chain M": "517",
    
    "6NR9: chainLength 1 in chain N": "515",
    
    "6NR9: chainLength 1 in chain O": "514",
    
    "6NR9: chainLength 1 in chain P": "514"
    
    }

    the results are also saved in output.txt

}
