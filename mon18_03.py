import requests
import xmltodict
import urllib2
import json

#uniprot
base_uni='https://www.uniprot.org/uniprot/P12345'


#query to print gene name
query_uniGeneName="&limit=1&format=xml"
url_uniGeneName =  base_uni + query_uniGeneName
u = requests.get(url_uniGeneName)
docGeneName = xmltodict.parse(u.content)
print "\nGene Name: "
print json.dumps(docGeneName['uniprot']['entry']['gene']['name']['#text'], indent = 4),"\n"

#query to print organism name
query_uniOrg="&limit=1&format=xml"
url_uniOrg =  base_uni + query_uniOrg
u = requests.get(url_uniOrg)
docOrgName = xmltodict.parse(u.content)
print "\nOrganism Name: "
print json.dumps( docOrgName['uniprot']['entry']['organism']['name'][0]['#text'], indent=4),"\n"
#print json.dumps( docOrgName['uniprot']['entry']['organism']['name'][1]['#text'], indent=4),"\n"

#query to print protein name
query_uniPro="&limit=1&format=xml"
url_uniPro =  base_uni + query_uniPro
u = requests.get(url_uniPro)
docProName = xmltodict.parse(u.content)
print "\nProtein Full Name:"
print json.dumps( docProName['uniprot']['entry']['protein']['recommendedName']['fullName'], indent=4),"\n"

#query to print comments
query_uniCom="&limit=1&format=xml"
url_uniCom =  base_uni + query_uniCom
u = requests.get(url_uniCom)
docComment = xmltodict.parse(u.content)
print "\nComments:"
print json.dumps( docComment['uniprot']['entry']['comment'][0]['text']['#text'], indent=4),"\n"

#query to print organism name
query_uniOrgId="&limit=1&format=xml"
url_uniOrgId =  base_uni + query_uniOrgId
u = requests.get(url_uniOrgId)
docOrgId = xmltodict.parse(u.content)
print "\nOrganism Id: "
print json.dumps( docOrgId['uniprot']['entry']['organism']['dbReference']['@id'], indent=4)

#query to print protein seq
query_uniProteinSeq="&columns=id,sequence&format=xml"
url_uniProteinSeq =  base_uni + query_uniProteinSeq
u = requests.get(url_uniProteinSeq)
docProteinSeq = xmltodict.parse(u.content)
print "\nProtein Sequence: "
print docProteinSeq['uniprot']['entry']['sequence']['#text'],"\n"


