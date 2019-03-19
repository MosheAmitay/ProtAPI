import requests
#making URLs to insert into requests
#uniprot
base_uni='https://www.uniprot.org/uniprot/'

#query_uni="?query=insulin&sort=score&columns=id,entry name,reviewed,protein names,genes,organism,length&limit=1&format=xml"
query_uni="?query=insulin&columns=id,sequence&limit=1&format=xml"
url_uni =  base_uni + query_uni
#url2 ='https://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&random=yes&format=xml'
u = requests.get(url_uni)
#print(u.headers)


#pdb
base_pdb='http://www.rcsb.org/pdb/rest/customReport.xml?'
query_pdb="pdbids=1stp,2jef,1cdg&customReportColumns=structureId,releaseDate,structureAuthor,pubmedId,doi&primaryOnly=1&service=wsfile&format=xml"
url_pdb =  base_pdb + query_pdb

#d = requests.get(url_pdb)
#print(d.content)




import xmltodict
import urllib2
import json

#download xml from pdb with wanted columns and pretty print

#filedata = urllib2.urlopen(url_pdb)
#datatowrite = filedata.read()

doc = xmltodict.parse(u.content)
#doc = d.content
#print json.dumps(doc, indent = 4)
#print doc['uniprot']['entry']['sequence']
print json.dumps(doc['uniprot']['entry']['sequence'], indent = 4)
print doc['uniprot']['entry']['sequence']['#text']
#print doc['dataset']['record'][0]['dimStructure.structureId']
