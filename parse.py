import requests
import xmltodict
import urllib2
import json
import os
import sys
import xml.etree.ElementTree as ET

GivenId=sys.argv[1]


base_uni='https://www.uniprot.org/uniprot/'
query="?query=id:"+GivenId+"&limit=1&format=xml"
url_general =  base_uni + query
u = requests.get(url_general)
entery = xmltodict.parse(u.content)
my_file=open("Doc.xml","w")
my_file.write(u.content)
my_file.close()

tree = ET.parse("Doc.xml") 
  
    # get root element 
root = tree.getroot() 
  
    # create empty list for news items 
newsitems = [] 
  
    # iterate news items 
    for item in root.findall('./channel/item'): 
  
        # empty news dictionary 
        news = {} 
  
        # iterate child elements of item 
	for child in item: 
  
		# special checking for namespace object content:media 
        	if child.tag == '{http://search.yahoo.com/mrss/}content': 
                	news['media'] = child.attrib['url'] 
       		else: 
        		news[child.tag] = child.text.encode('utf8') 
  
        # append news dictionary to news items list 
newsitems.append(news) 

# return news items list 
return newsitems
