'''
YNpdb: A Python Rest_API for the RCSB Protein Data Bank. 
Written by Yiska Neriya, 2019.
'''

import requests, xmltodict, urllib2, json

'''
=================
A function that helps the function 'search_pdb()'
=================
'''

def find_columns_and_ids(listIds,listColumns,doc):
'''Passes on the dictionary 'doc' and puts nicely the values of it in a new dictionary 

   Parameters
    ----------
    listIds : list of strings
        A list of 4 character strings giving a pdb entry
    listColumns: list of strings
        A list of valuse that can search for in the pdb
    doc : dictionary or list of dictionaries
        A dictionary or list of dictionaries
    Returns
    -------
    out : OrderedDict
        An ordered dictionary object corresponding to bare xml
    '''

#gets a list of ids, list of columns, dictionary or list of dictionaries
#returns a list of the results

#'a help function: gets a list of ids, list of columns, dictionary or list of dictionaries returns a list of the results'
        result_dict = dict()
        j = 0
        #the loop passes on the list of columns
        #try:if the entry of the column is 'dimStructure'- it will put the value in the result dictionry onder the parent 'di$
        #except:if it gives an error- puts the value in the result dictionry onder the parent 'dimEntity'
        while j < len(listColumns):
          if type(doc)==list: #'doc' is a list
             for d in doc: #passes on the dictionaries that are in the list "doc"
               try:
                   result_dict['%s: %s' %(d["dimEntity.structureId"],listColumns[j])]=d['dimStructure.%s' %listColumns[j]]
               except:
                      result_dict['%s: %s in chain %s' %(d["dimEntity.structureId"],listColumns[j],d["dimEntity.chainId"])]=d['dimEntity.%s' %listColumns[j]]
          else: #'doc' is a dictionary
             try:
               result_dict['%s: %s' %(doc["dimEntity.structureId"],listColumns[j])]=doc['dimStructure.%s' %listColumns[j]]
             except:
               result_dict['%s: %s in chain %s' %(doc["dimEntity.structureId"],listColumns[j],doc["dimEntity.chainId"])]=doc['dimEntity.%s' %listColumns[j]]
          j=j+1
        return result_dict
        
'''
=================
Function for looking up information given PDB ids and columns
=================
'''        
        
def search_pdb(url_root='http://www.rcsb.org/pdb/rest/customReport.xml?'):
'''Passes on the dictionary 'doc' and puts nicely the values of it in a new dictionary 

   Parameters
    ----------
    url_root : string
        The string root of the specific url for the request type
    Returns
    -------
    out : OrderedDict
        An ordered dictionary object corresponding to bare xml
    '''

#'askes for ids and columns and prints the information about them arranged'

        ids = input('Enter the ids that you are interested in (separated by commas): ')
        columns = input('Enter the columns that you are interested in (separated by commas): \n choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ')

        #pdbids- the ids of the entry, customReportColumns-the values that you want to find, format- returnd type
        query_pdb="pdbids=%s&customReportColumns=%s&format=xml" %(ids, columns)

        url_pdb = url_root + query_pdb #the final url
        d = requests.get(url_pdb) #download xml result of the url from pdb with wanted columns
        doc = xmltodict.parse(d.content) #converts from xml to dictionary
        doc = doc['dataset']['record'] #puts the beginning in the dictionary
        #print json.dumps(doc,indent=4) #prints to the screen the results in a dictionary in format json the dictionary of the output
        ids = ids.split(",")
        columns = columns.split(",")
        result_dict = find_columns_and_ids(ids,columns,doc)
        print '\n',json.dumps(result_dict,indent=4, sort_keys=True) #prints the results


