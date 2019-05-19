import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def parseGeo(accFile, field):
    data = pd.read_csv(accFile, sep="\n", header=None) #read the content
    data.columns = ["accession"]
    output=open('output.txt', 'w')
    for a in data["accession"]: #for each ID
            url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+a
            source=requests.get(url).text #get the html page
            soup=bs(source,'lxml')
            if soup.find_all("td"):
                    for element in soup.find_all("td"):
                            if element.string==field: #find the wanted line
                                    output.write("%s\n" % strip_non_ascii(element.next_sibling.next_sibling.text))
    output.close()
    print("the results are in output.txt")
def parse(db, accFile, field):
    if db=="geo":
      parseGeo(accFile, field)
      
db=raw_input("please enter the database you need:   ")
accFile=raw_input("please enter name of a file with the accessions:   ")
field=raw_input("please enter the field your'e interested in extracting:   ")
parse(db, accFile, field)
