#!/usr/bin/env python
import xmltodict
import urllib2
import json
import requests

#download xml from pdb with wanted columns and pretty print
urlUP = 'https://www.uniprot.org/uniprot/?query=insulin&sort=score&columns=id,entry name,reviewed,protein names,genes,organism,length&format=xml'
url ='https://www.rcsb.org/pdb/rest/customReport.xml?pdbids=1stp,&customReportColumns=structureId,structureTitle,sequence&service=wsfile&format=xml'
response = requests.get("https://www.uniprot.org/uniprot/P12345.xml")
datatowrite  = response.content

#filedata = urllib2.urlopen(urlUP)
#datatowrite = filedata.read()

doc = xmltodict.parse(datatowrite)
print json.dumps(doc, indent = 4)
#print doc['dataset']['record']['dimEntity.sequence']

