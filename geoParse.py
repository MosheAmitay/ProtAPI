import os,sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

fname=sys.argv[1] #you need to enter the filename of the IDs
data = pd.read_csv(fname, sep="\n", header=None) #read the content
data.columns = ["accession"]
platforms=[]
for a in data["accession"]: #for each ID
        url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+a
        source=requests.get(url).text #get the html page
        soup=bs(source,'lxml')
        if soup.find_all("td"):
                for element in soup.find_all("td"):
                        if element.string=="Title": #find the wanted line
                                platforms.append(strip_non_ascii(element.next_sibling.next_sibling.string))
with open('output.txt', 'w') as f:
    for item in platforms:
        f.write("%s\n" % item)
print("the results are in output.txt")
