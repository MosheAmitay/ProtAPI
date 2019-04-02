import requests
import xmltodict
import urllib2
import json
import os
import sys
GivenId=sys.argv[1]

#uniprot

#base_uni='https://www.uniprot.org/uniprot/P12345'

base_uni='https://www.uniprot.org/uniprot/'
query="?query=id:"+GivenId+"&limit=1&format=xml"
url_general =  base_uni + query
u = requests.get(url_general)
entery = xmltodict.parse(u.content)





Full_Dict={
"Gene Name:": entery['uniprot']['entry']['gene']['name']['#text'],
"Organism Name:": entery['uniprot']['entry']['organism']['name'][0]['#text'],
"Protein Full Name:": entery['uniprot']['entry']['protein']['recommendedName']['fullName'],
"Comments:": entery['uniprot']['entry']['comment'][0]['text']['#text'],
"Protein Sequence:": entery['uniprot']['entry']['sequence']['#text'],
"Data Set:": json.dumps(entery['uniprot']['entry']['@dataset'], indent=4),
"Date Of Creation:": json.dumps(entery['uniprot']['entry']['@created'], indent=4),
"Date Of Last Modification:": json.dumps(entery['uniprot']['entry']['@modified'], indent=4)



}
for x, y in Full_Dict.items():
        print"\n"
        print(x, y)

