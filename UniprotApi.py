import requests
import xmltodict
import urllib2
import json
import os
import sys
__metaclass__=type

class Uniprot:
	entry=[]
	accession=[]
	def __init__(self):
                GivenIds=raw_input("Please Enter Accession Numbers (seperated by spaces):    ")
                list =GivenIds.split()
		base_uni='https://www.uniprot.org/uniprot/'
		for acc in list:
			self.accession.append(acc)
			query="?query=id:"+acc+"&columns=id,entry name&limit=1&format=xml"
			url_general =  base_uni + query
			u = requests.get(url_general)
			self.entry.append( xmltodict.parse(u.content))

	def GeneName(self):
		j=0
		for i in self.entry:
                	if isinstance(i['uniprot']['entry']['gene']['name'],list):
                        	print "\nGene Name Of " + self.accession[j] + ": " + i['uniprot']['entry']['gene']['name'][0]['#text']
				j=j+1
                	else:
				print "\nGene Name of " + self.accession[j] + ": " + i['uniprot']['entry']['gene']['name']['#text']
				j=j+1
	def Title(self):
		j=0
		for i in self.entry:
                	print "\nTitle Of " + self.accession[j] + ": " + i['uniprot']['entry']['reference'][0]['citation']['title']
			j=j+1
	def ProteinName(self):
		j=0
		for i in self.entry:
                	print "\nProtein Name Of " + self.accession[j] + ": " + i['uniprot']['entry']['protein']['recommendedName']['fullName']
			j=j+1
	def Organism(self):
		j=0
		for i in self.entry:
                	print "\nOrganism Of " + self.accession[j] + ": " + i['uniprot']['entry']['organism']['name'][0]['#text']
			j=j+1
	def ProteinSeq(self):
		j=0
		for i in self.entry:
                	print "\nProtein Sequence Of " +self.accession[j] +":\n\n" + i['uniprot']['entry']['sequence']['#text']
			j=j+1
	def Modified(self):
		j=0
                i=0
		Mod_Dict={}
		for a in self.entry:
                	for x in a['uniprot']['entry']['feature']:
                        	if x['@type']=='modified residue':
                                	i=i+1
                                	Mod_Dict['Modification number '+str(i)]='Description= '+x['@description']
			print "\nModified Genes Of " +self.accession[j] + ":\n"
			j=j+1
                	print(json.dumps(Mod_Dict, indent=4, sort_keys=True))

        def Variations(self):
		i=0
                j=0
		Seq_Var_Dict={}
		for a in self.entry:
                	for x in a['uniprot']['entry']['feature']:
                        	if x['@type']=='sequence variant':
                                 	j=j+1
                                 	Seq_Var_Dict['Sequence Varient '+str(j)]=x['original']+' Turns to '+x['variation']+'at position: '+ x['location']['position']['@position']
			print "\nVariations Of " +self.accession[i] + ":\n"
			i=i+1
                	print(json.dumps(Seq_Var_Dict, indent=4, sort_keys=True))
	def PrintAll(self):		
           		self.GeneName()
               		self.Title()
                	self.ProteinName()
                	self.Organism()
                	self.ProteinSeq()
                #	self.Modified()
                #	self.Variations()

