#YNpdb: A Python Rest_API for the RCSB Protein Data Bank.
#Written by Yiska Neriya, 2019.

#Bioinformatics, Jerusalem College of Technology (JCT) Tal-Campus, 2019.


import requests, xmltodict, urllib2, json, os



#=================
#Functions for looking up information given PDB ids and columns
#=================

def search_pdb(url_root='http://www.rcsb.org/pdb/rest/customReport.xml?'):
#askes for ids and columns and prints the information about them arranged

#    Parameter
#    ----------
#    url_root : string
#    The string root of the specific url for the request type

#    Prints
#    -------
#    result_dict : dictionary
#    A nice and ordered dictionary of the ids and the columns

#    Example
#    --------
#    Enter the ids that you are interested in (separated by commas): 6Q9Q
#    Enter the columns that you are interested in (separated by commas):
#    choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ligandName

#{
#    "6Q9Q: ligandName in chain A": "1,4,7,10,13,16-HEXAOXACYCLOOCTADECANE",
#    "6Q9Q: ligandName in chain B": "SULFATE ION",
#    "6Q9Q: ligandName in chain C": "SULFATE ION",
#    "6Q9Q: ligandName in chain D": "SULFATE ION"
#}


        ids = raw_input('Enter the ids that you are interested in (separated by commas): ')
        columns = raw_input('Enter the columns that you are interested in (separated by commas): \n choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ')

        #pdbids- the ids of the entry, customReportColumns-the values that you want to find, format- returnd type
        query_pdb="pdbids=%s&customReportColumns=%s&format=xml" %(ids, columns)

        url_pdb = url_root + query_pdb #the final url
        d = requests.get(url_pdb) #download xml result of the url from pdb with wanted columns
        doc = xmltodict.parse(d.content)
        try:
          doc = doc['dataset']['record'] #puts the beginning in the dictionary
          ids = ids.split(",")
          columns = columns.split(",")
          result_dict = dict()

          j = 0
          while j < len(columns):
            if type(doc)==list: #'doc' is a list of dictionaries
               for d in doc:
                 #try:if the entry of the column is 'dimStructure'- it will put the value in the result dictionry onder the parent 'dimStructure'
                 try:
                     result_dict['%s: %s' %(d["dimEntity.structureId"],columns[j])]=d['dimStructure.%s' %columns[j]]
                 #except:if it gives an error- puts the value in the result dictionry onder the parent 'dimEntity'
                 except:
                        result_dict['%s: %s in chain %s' %(d["dimEntity.structureId"],columns[j],d["dimEntity.chainId"])]=d['dimEntity.%s' %columns[j]]
            else: #'doc' is a dictionary
               try:
                 result_dict['%s: %s' %(doc["dimEntity.structureId"],columns[j])]=doc['dimStructure.%s' %columns[j]]
               except:
                 result_dict['%s: %s in chain %s' %(doc["dimEntity.structureId"],columns[j],doc["dimEntity.chainId"])]=doc['dimEntity.%s' %columns[j]]
            j=j+1

          output=open('output.txt', 'w') #a file for saveing the results
          output.write("\n%s" %json.dumps(result_dict,indent=4, sort_keys=True))
          output.close()
          print '\n',json.dumps(result_dict,indent=4, sort_keys=True)
          print("\n\nthe results are also saved in output.txt\n")
        except:
          print '\n',"There is no information abuot this column/s"



def print_all(url_root='http://www.rcsb.org/pdb/rest/customReport.xml?'):
#askes for ids and columns and prints the full records as a dictionary

#    Parameter
#    ----------
#    url_root : string
#    The string root of the specific url for the request type

#    Prints
#    -------
#    doc : dictionary
#    A dictionary of the full records

#    Example
#    --------
#    Enter the ids that you are interested in (separated by commas): 5NUU
#    Enter the columns that you are interested in (separated by commas):
#    choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: taxonomyId

#{
#    "dimEntity.structureId": "5NUU",
#    "dimEntity.chainId": "A",
#    "dimEntity.taxonomyId": "7787"
#}
        ids = raw_input('Enter the ids that you are interested in (separated by commas): ')
        columns = raw_input('Enter the columns that you are interested in (separated by commas): \n choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ')

        #pdbids- the ids of the entry, customReportColumns-the values that you want to find, format- returnd type
        query_pdb="pdbids=%s&customReportColumns=%s&format=xml" %(ids, columns)

        url_pdb = url_root + query_pdb #the final url
        d = requests.get(url_pdb) #download xml result of the url from pdb with wanted columns
        doc = xmltodict.parse(d.content)

        try:
          doc = doc['dataset']['record'] #puts the beginning in the dictionary
          output=open('output.txt', 'w') #a file for saveing the results
          output.write("\n%s" %json.dumps(doc,indent=4))
          output.close()
          print '\n',json.dumps(doc,indent=4)
          print("\n\nthe results are also saved in output.txt\n")
        except:
          print '\n',"There is no information abuot this column/s"

