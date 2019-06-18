#this code fetches information from several databases by beautifulSoup
import requests #for communicating with web
import pandas as pd #for managing data
from bs4 import BeautifulSoup as bs #for scraping the web-pages

#the function recieves a string and returns only ascii coded characters
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

#this function is specific to NCBI's geo database
#it gets a file with accession numbers and a requested field
#the results are entered to a file in the order of the accessions recieved
def parseGeo(accFile, field):
    data = pd.read_csv(accFile, sep="\n", header=None) #read the content with pandas
    data.columns = ["accession"]
    output=open('output.txt', 'w') #open a file for output
    for a in data["accession"]: #for each ID
            url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+a
            source=requests.get(url).text #get the html page
            soup=bs(source,'lxml') #create beautiful soup object
            if soup.find_all("td"): #if the search exists
                    for element in soup.find_all("td"):
                            if element.string==field: #find the wanted line
				#put the information into the file
                                    output.write("%s\n" % strip_non_ascii(element.next_sibling.next_sibling.text))
    output.close()
    print("the results are in output.txt")

def parseSRA(accFile, field):
    data = pd.read_csv(accFile, sep="\n", header=None) #read the content with pandas
    data.columns = ["accession"]
    output=open('output.txt', 'w') #open a file for output
    for a in data["accession"]: #for each ID
	    if "SRX" in a: parseSRX(a)
            
def parseSRX(acc):
	url = 'https://www.ncbi.nlm.nih.gov/sra/'+acc+'[accn]'
        source=requests.get(url).text #get the html page
        soup=bs(source,'lxml') #create beautiful soup object
        if soup.find_all("div"):
                for element in soup.find_all("div"):
                        if field in element.text:if field=='Library':
                                if field=='Library':
                                        for item in element.div:
                                               output_file.write("%s\n" % strip_non_ascii(item.contents[0]+item.span.text))
                                elif field=='Runs':
                                        output_file.write("%s\n" % strip_non_ascii(element.span.contents[0])) 
                                        table=element.next_sibling
                                        for row in range(len(table.tbody.contents)):
                                                for col in range(len(table.thead.tr.contents)):
                                                        if col == 0:
                                                                output_file.write("%s\n" % strip_non_ascii(table.thead.tr.contents[col].text+" #"+str(row+1)+": "+table.tbody.contents[row].contents[col].text))
                                                        else:
                                                                output_file.write("%s\n" % strip_non_ascii(table.thead.tr.contents[col].text+": "+table.tbody.contents[row].contents[col].text))
                                else:
					output_file.write("%s\n" % strip_non_ascii(element.span.contents[0]))

#this is a redirection function for future expansions
def parse(db, accFile, field):
    if db=="geo":
        parseGeo(accFile, field)
    if db=="sra":
	parseSRA(accFile, field)

#here you get the information for the functions
db=raw_input("please enter the database you need:   ")
accFile=raw_input("please enter name of a file with the accessions:   ")
field=raw_input("please enter the field your'e interested in extracting:   ")
parse(db, accFile, field)