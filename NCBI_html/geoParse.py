#this code fetches information from several databases by beautifulSoup
import requests #for communicating with web
import pandas as pd #for managing data
from bs4 import BeautifulSoup as bs #for scraping the web-pages
import json
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
    values=dict()
    output=open('output.txt', 'w') #open a file for output
    for a in data["accession"]: #for each ID
            numFound=0
            url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+a
            source=requests.get(url).text #get the html page
            soup=bs(source,'lxml') #create beautiful soup object
            if soup.find_all("td"): #if the search exists
                    for element in soup.find_all("td"):
                            if field in element.text and numFound==0 and not(element.strong): 
                            #find the wanted line, and do not repeat for same field
                            #also, an element with 'strog' attribute does not fit to our fields. (with exeption to the table, to be handled)
                                    if "Samples" in field:
                                            if "Samples (" in element.text: #must have a () with the number inside 
                                                    all=""
                                                    for sample in element.next_sibling.next_sibling.find_all('a'):
                                                    #concatenate the strings from the a tags - the links
                                                            all=all+sample.string+", "
                                                            #print(sample.string)
                                                    values[a+"_"+field]=strip_non_ascii(all[0:-2])
                                                    output.write("%s\n" % strip_non_ascii(all[0:-2]))
                                                    numFound=numFound+1
                                    else:
				                                    #put the information into the file or dictionary
                                            numFound=numFound+1
                                            values[a+"_"+field] = strip_non_ascii(element.next_sibling.next_sibling.text)
                                            output.write("%s\n" % strip_non_ascii(element.next_sibling.next_sibling.text))
    output.close()
    print("the results are in output.txt")
    return values

def parseSRA(accFile, field):
    data = pd.read_csv(accFile, sep="\n", header=None) #read the content with pandas
    data.columns = ["accession"]
    values=dict()
    output=open('output.txt', 'w') #open a file for output
    for a in data["accession"]: #for each ID
	    if "SRX" in a: parseSRX(a,output,values)
    output.close()
    print("the results are in output.txt")
    return values
            
def parseSRX(acc,output_file,values):
        url = 'https://www.ncbi.nlm.nih.gov/sra/'+acc+'[accn]'
        source=requests.get(url).text #get the html page
        soup=bs(source,'lxml') #create beautiful soup object
        if soup.find("div", {"id": "ResultView"}): #if the data exists
                for element in soup.find("div", {"id": "ResultView"}): #loop over the data and find the needed field
                        if field in element.text:
                                if field=='Library': #needs special data extraction
                                        all=''
                                        for item in element.div:
                                                #write the title=contents[0] and the content=item.span.text
                                                all=all+strip_non_ascii(item.contents[0]+item.span.text)+"\n"
                                                output_file.write("%s\n" % strip_non_ascii(item.contents[0]+item.span.text))
                                        values[acc+"_"+field]=all
                                elif field=='Runs': #needs special data extraction
                                        #write the header
                                        all=strip_non_ascii(element.span.contents[0])+"\n"
                                        output_file.write("%s\n" % strip_non_ascii(element.span.contents[0])) 
                                        table=element.next_sibling
                                        for row in range(len(table.tbody.contents)):
                                                for col in range(len(table.thead.tr.contents)):
                                                        if col == 0:
                                                                #if it is the Run cell
                                                                all=all+strip_non_ascii(table.thead.tr.contents[col].text+" #"+str(row+1)+": "+table.tbody.contents[row].contents[col].text)+"\n"
                                                                output_file.write("%s\n" % strip_non_ascii(table.thead.tr.contents[col].text+" #"+str(row+1)+": "+table.tbody.contents[row].contents[col].text))
                                                        else:
                                                                all=all+strip_non_ascii(table.thead.tr.contents[col].text+": "+table.tbody.contents[row].contents[col].text)+"\n"
                                                                output_file.write("%s\n" % strip_non_ascii(table.thead.tr.contents[col].text+": "+table.tbody.contents[row].contents[col].text))
                                        values[acc+"_"+field]=all
                                else:
                                        values[acc+"_"+field]=strip_non_ascii(element.span.contents[0])
                                        output_file.write("%s\n" % strip_non_ascii(element.span.contents[0]))

#this is a redirection function for future expansions
def parse(db, accFile, field):
    if db=="geo":
        return parseGeo(accFile, field)
    if db=="sra":
	      return parseSRA(accFile, field)

#here you get the information for the functions
db = raw_input("please enter the database you need:   ")
accFile = raw_input("please enter name of a file with the accessions:   ")
field = raw_input("please enter the field your'e interested in extracting:   ")
print json.dumps(parse(db, accFile, field), indent=4)
