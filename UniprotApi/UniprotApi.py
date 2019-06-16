import requests
import xmltodict
import json
import pandas as pd

__metaclass__=type

class UniprotApi:
	entry=[]
	accession=[]
	list=[]
	def __init__(self,accList):
		base_uni='https://www.uniprot.org/uniprot/'
		for acc in accList:
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
			if len(Mod_Dict)==0:
				print "There are no modified genes"
			else:
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
		
		for i in range(len(self.entry)):
			print "\nInformation for accession number: "+ self.accession[i]
			
			#gene name
			if isinstance(self.entry[i]['uniprot']['entry']['gene']['name'],list):
                               	print "\nGene Name: "  + self.entry[i]['uniprot']['entry']['gene']['name'][0]['#text']
                        else:
                                print "\nGene Name of "+ self.entry[i]['uniprot']['entry']['gene']['name']['#text']
			#title
			print "\nTitle Of " + ": " + self.entry[i]['uniprot']['entry']['reference'][0]['citation']['title']

			#protein
                        print "\nProtein Name Of " + ": " + self.entry[i]['uniprot']['entry']['protein']['recommendedName']['fullName']

			#organism
		        print "\nOrganism Of " + ": " + self.entry[i]['uniprot']['entry']['organism']['name'][0]['#text']

			#protein sequence
			print "\nProtein Sequence Of " +":\n\n" + self.entry[i]['uniprot']['entry']['sequence']['#text']

	
			a=0
			
			Mod_Dict={}


			for x in self.entry[i]['uniprot']['entry']['feature']:
                                if x['@type']=='modified residue':
                                        a=a+1
                                        Mod_Dict['Modification number '+str(a)]='Description= '+x['@description']
                        print "\nModified Genes Of " +self.accession[i] + ":\n"
          
			if len(Mod_Dict)==0:
                                print "There are no modified genes"
                        else:
                                print(json.dumps(Mod_Dict, indent=4, sort_keys=True))
			b=0
			Seq_Var_Dict={}
                        for x in self.entry[i]['uniprot']['entry']['feature']:
                                if x['@type']=='sequence variant':
                                        b=b+1
                                        Seq_Var_Dict['Sequence Varient '+str(b)]=x['original']+' Turns to '+x['variation']+'at position: '+ x['location']['position']['@position']
                        print "\nVariations Of " +self.accession[i] + ":\n"
                        
                        print(json.dumps(Seq_Var_Dict, indent=4, sort_keys=True))
