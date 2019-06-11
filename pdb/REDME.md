# YNpdb
A Python Rest_API for the RCSB Protein Data Bank

YNpdb includs two functions:
1. search_pdb()- gets pdb ids and columns(records) of interest 
                 and prints and returns the information about them arranged as a dictionary.
2. print_all()- gets pdb ids and columns(records) of interest 
                and prints and returns the full records as a dictionary.
                

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

---------------------------------------

### print_all()

1.

ids = ['6EGC']

columns = ['atomSiteCount']

dict_1 = YNpdb.print_all(ids, columns)

{


    {

    "dimStructure.structureId": "6EGC",
    
    "dimStructure.atomSiteCount": "1134"

    }

    the results are also saved in output.txt

}

-----------------------------------
2.

ids = ['6QN9','6DJH']

columns = ['ligandName']

dict_1 = YNpdb.print_all(ids, columns)

{

    [

        {
    
        "dimEntity.structureId": "6QN9",
        
        "dimEntity.chainId": "L",
        
        "dimEntity.ligandName": "GLYCEROL",
        
        },
    
        {
    
        "dimEntity.structureId": "6QN9",
        
        "dimEntity.chainId": "H",
        
        "dimEntity.ligandName": "null",

        },
    
        {
    
        "dimEntity.structureId": "6QN9",
        
        "dimEntity.chainId": "L",
        
        "dimEntity.ligandName": "SULFATE ION",
        
        },
    
        {
    
        "dimEntity.structureId": "6DJH",
        
        "dimEntity.chainId": "B",
        
        "dimEntity.ligandName": "8-bromo-4-oxo-1,4-dihydroquinoline-3-carboxylic acid",

        },
    
        {
    
        "dimEntity.structureId": "6DJH",
        
        "dimEntity.chainId": "A",
        
        "dimEntity.ligandName": "1,2-ETHANEDIOL",
        
        },
    
        {
    
        "dimEntity.structureId": "6DJH",
        
        "dimEntity.chainId": "B",
        
        "dimEntity.ligandName": "1,2-ETHANEDIOL",

        },
    
        {
        "dimEntity.structureId": "6DJH",
        
        "dimEntity.chainId": "A",
        
        "dimEntity.ligandName": "8-bromo-4-oxo-1,4-dihydroquinoline-3-carboxylic acid",

        }
    
    ]

    the results are also saved in output.txt

}

