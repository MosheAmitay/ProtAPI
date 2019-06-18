#YNpdb: A Python Rest API for the RCSB Protein Data Bank.
#Written by Yiska Neriya, 2019.

#Bioinformatics, Jerusalem College of Technology (JCT) Tal-Campus, 2019.


import requests, xmltodict, urllib2, json, os

def search_pdb(ids, columns, url_root='http://www.rcsb.org/pdb/rest/customReport.xml?'):
#askes for ids and columns and prints the information about them arranged

#    Parameter
#    ----------
#    url_root : string
#       The string root of the specific url for the request type

#    columns : list
#       A list of strings of pdb columns

#    ids : list
#       A list of strings of pdb ids

#    Returns & Prints
#    -----------------
#    result_dict : dictionary
#    A nice and ordered dictionary of the ids and the columns

#    Example
#    --------

#{
#    "6Q9Q: ligandName in chain A": "1,4,7,10,13,16-HEXAOXACYCLOOCTADECANE",
#    "6Q9Q: ligandName in chain B": "SULFATE ION",
#    "6Q9Q: ligandName in chain C": "SULFATE ION",
#    "6Q9Q: ligandName in chain D": "SULFATE ION"
#}

        str_ids = ','.join(ids) #converts the list of ids into a string
        str_columns = ','.join(columns) #converts the list of columns into a string

        #pdbids- the ids of the entry, customReportColumns-the values that you want to find, format- returnd type
        query_pdb="pdbids=%s&customReportColumns=%s&format=xml" %(str_ids,str_columns)
        url_pdb = url_root + query_pdb #the final url
        d = requests.get(url_pdb) #download xml result of the url from pdb with wanted columns
        doc = xmltodict.parse(d.content)
        result_dict = dict()
        try:
          doc = doc['dataset']['record'] #puts the beginning in the dictionary
          j = 0
          output=open('output.txt', 'w') #a file for saveing the results
          while j < len(columns):
            if type(doc)==list: #'doc' is a list of dictionaries
               for d in doc:
                 #try:if the entry of the column is 'dimStructure'- it will put the value in the result dictionry onder the parent 'dimStructure'
                 try:
                     result_dict['%s: %s' %(d["dimEntity.structureId"],columns[j])]=d['dimStructure.%s' %columns[j]]
                     output.write("%s\n" %(d["dimEntity.structureId"]+": "+columns[j]+": "+d['dimStructure.%s' %columns[j]]))
                 #except:if it gives an error- puts the value in the result dictionry onder the parent 'dimEntity'
                 except:
                        result_dict['%s: %s in chain %s' %(d["dimEntity.structureId"],columns[j],d["dimEntity.chainId"])]=d['dimEntity.%s' %columns[j]]
                        output.write("%s\n" %(d["dimEntity.structureId"]+": "+columns[j]+" in chain "+d["dimEntity.chainId"]+": "+d['dimEntity.%s' %columns[j]]))
            else: #'doc' is a dictionary
               try:
                 result_dict['%s: %s' %(doc["dimStructure.structureId"],columns[j])]=doc['dimStructure.%s' %columns[j]]
                 output.write("%s\n" %(doc["dimStructure.structureId"]+": "+columns[j]+": "+doc['dimStructure.%s' %columns[j]]))
               except:
                 result_dict['%s: %s in chain %s' %(doc["dimEntity.structureId"],columns[j],doc["dimEntity.chainId"])]=doc['dimEntity.%s' %columns[j]]
                 output.write("%s\n" %(doc["dimEntity.structureId"]+": "+columns[j]+" in chain "+doc["dimEntity.chainId"]+": "+doc['dimEntity.%s' %columns[j]]))
            j=j+1

          #output.write("%s\n" %json.dumps(result_dict,indent=4, sort_keys=True))
          output.close()
          print '\n',json.dumps(result_dict,indent=4, sort_keys=True)
          print("\nthe results are also saved in output.txt\n")
        except:
          print '\n',"There is no information abuot this column/s"
        return result_dict
