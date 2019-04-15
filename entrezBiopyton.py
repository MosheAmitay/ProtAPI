import xmltodict
import urllib2
import json

from Bio import Entrez
Entrez.email = "shirliya207@gmail.com"

#handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
#print(handle.readline().strip())
#handle = Entrez.esearch(db="pubmed", term="biopython")
#record = Entrez.read(handle)
#handle.close()
#print(record.keys())
#print(record["IdList"])
#handle = Entrez.esummary(db = "pubmed", id = "24929426")
#record = Entrez.read(handle)

#print(record)

#handle = Entrez.efetch(db = "nucleotide",id = "EU490707", rettype = "gb", retmode = "text")
#print(handle.read()


#download xml from pdb with wanted columns and pretty print
url ='https://www.rcsb.org/pdb/rest/customReport.xml?pdbids=1stp,&customReportColumns=structureId,structureTitle,sequence&service=wsfile&format=xml'
filedata = urllib2.urlopen(url)
datatowrite = filedata.read()

doc = xmltodict.parse(datatowrite)
print json.dumps(doc, indent = 4)
#print doc['dataset']['record']['dimEntity.sequence']

