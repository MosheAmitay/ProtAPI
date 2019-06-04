# YNpdb
A Python Rest_API for the RCSB Protein Data Bank

YNpdb includs two functions:
1. search_pdb()- askes for pdb ids and columns(records) of interest 
                 and prints and returns the information about them arranged as a dictionary.
2. print_all()- askes for pdb ids and columns(records) of interest 
                and prints and returns the full records as a dictionary.
                

## Install
For using my library you must install the libraries: requests, xmltodict, urllib2, json, os
## Examples
### search_pdb()

The code for this function:

search = YNpdb.search_pdb()

#### outputs
-------------------------------
1.
{

    Enter the ids that you are interested in (separated by commas): 5NUU

    Enter the columns that you are interested in (separated by commas):
     choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: taxonomyId

    {

     "5NUU: taxonomyId in chain A": "7787"
    
    }

    the results are also saved in output.txt

}

-----------------------------
2.
{

      Enter the ids that you are interested in (separated by commas): 6GUS

      Enter the columns that you are interested in (separated by commas):
       choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: chainLength,ligandId

    {

    "6GUS: chainLength in chain A": "155",
    
    "6GUS: ligandId in chain A": "SO4"
    
    }

    the results are also saved in output.txt
    
}

-----------------------------
3.
{

    Enter the ids that you are interested in (separated by commas): 6EGC
    
    Enter the columns that you are interested in (separated by commas):
     choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: sequence

    {

    "6EGC: sequence in chain A":         "GSHMTRTEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQQGPPGNEIIRELERSLREQEELAKRLKELLRELERLQREGSSDEDVRELLREIKELVEEIEKLAREQKYLVEELKRQD"

    }

    the results are also saved in output.txt

}

------------------------------
4.
{

    Enter the ids that you are interested in (separated by commas): 6QN9

    Enter the columns that you are interested in (separated by commas):
     choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: plasmid,doi

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

The code for this function:

all = YNpdb.print_all()

#### outputs
---------------------------------------
1.
{

    Enter the ids that you are interested in (separated by commas): 6EGC

    Enter the columns that you are interested in (separated by commas):
    choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: atomSiteCount

    {

    "dimStructure.structureId": "6EGC",
    
    "dimStructure.atomSiteCount": "1134"

    }

    the results are also saved in output.txt

}

-----------------------------------
2.
{

    Enter the ids that you are interested in (separated by commas): 6QN9,6DJH

    Enter the columns that you are interested in (separated by commas):
    choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ligandName

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
