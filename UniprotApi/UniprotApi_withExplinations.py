import requests # this is what i used to help me retrieve the data from uniprot using a url
import xmltodict
import json # this helps print a dictionary out nicely

__metaclass__=type

# this class is meant to help easily  retrieve data from Uniprot when given an accession number

class UniprotApi:
	entry=[] # this list stores all of the entry's that come from a url using a given accession number 
	accession=[] # this stores all of the given accession numbers
	def __init__(self,accList): #the init recieves a list of accessions called accList
                base_uni='https://www.uniprot.org/uniprot/'
                for acc in accList:
                        self.accession.append(acc) # here we add the accession numbers one by one to a new list called accession this is so we can 
				                   # later use the accessions in the other functions
                        query="?query=id:"+acc+"&columns=id,entry name&limit=1&format=xml" # here we build our query url containing an accession number 
                        url_general =  base_uni + query  # full url for requests including the base url + query containing an accession number
                        u = requests.get(url_general)  # here we use requests to retreive all data from uniprot based on the given accession number
                        self.entry.append( xmltodict.parse(u.content)) # we add the data that is organized into a dictionary into the 'entry' list

 
# from here on are the functions created to retreave spacific data:

	# this function returns the gene names of all the accession numbers 	
	def GeneName(self):
		j=0
		for i in self.entry:
			# since sometimes there are a few names to a given accession  numbers this if was neccissary 
                	if isinstance(i['uniprot']['entry']['gene']['name'],list):
				# ive asked that is there is more than one name to just print the first name in the list
                        	print "\nGene Name Of " + self.accession[j] + ": " + i['uniprot']['entry']['gene']['name'][0]['#text']
				j=j+1
                	else:
				print "\nGene Name of " + self.accession[j] + ": " + i['uniprot']['entry']['gene']['name']['#text']
				j=j+1
	# this function returns the title of all the accession numbers 
	def Title(self):
		j=0
		for i in self.entry:
                	print "\nTitle Of " + self.accession[j] + ": " + i['uniprot']['entry']['reference'][0]['citation']['title']
			j=j+1
	# this function returns the protein name of all the accession numbers 
	def ProteinName(self):
		j=0
		for i in self.entry:
                	print "\nProtein Name Of " + self.accession[j] + ": " + i['uniprot']['entry']['protein']['recommendedName']['fullName']
			j=j+1
	# this function finds the organism names of of all the accession numbers
	def Organism(self):
		j=0
		for i in self.entry:
                	print "\nOrganism Of " + self.accession[j] + ": " + i['uniprot']['entry']['organism']['name'][0]['#text']
			j=j+1
	#this function finds all the protein sequences for all of the accession numbers 
	def ProteinSeq(self):
		j=0
		for i in self.entry:
                	print "\nProtein Sequence Of " +self.accession[j] +":\n\n" + i['uniprot']['entry']['sequence']['#text']
			j=j+1
	# this function finds all the modified genes for all of the accession numbers
	def Modified(self):
		j=0
                i=0
		Mod_Dict={}
		for a in self.entry:
			# goes to the 'feature' place in the entry dictionary
                	for x in a['uniprot']['entry']['feature']:
				# in the 'feature' place looks to see if there are modified genes if there are then they are added to the Mod_Dict dictionary
                        	if x['@type']=='modified residue':
                                	i=i+1
                                	Mod_Dict['Modification number '+str(i)]='Description= '+x['@description']
			print "\nModified Genes Of " +self.accession[j] + ":\n"
			j=j+1
			# if there are no modified genes in specific accession number
			if len(Mod_Dict)==0:
				print "There are no modified genes"
			else:
                		print(json.dumps(Mod_Dict, indent=4, sort_keys=True))
	# this functon prints out all of the variations 
        def Variations(self):
		i=0
                j=0
		Seq_Var_Dict={}
		for a in self.entry:
                	for x in a['uniprot']['entry']['feature']:
				# if there are variations then they are added to the Seq_Var_Dict and later printed out 
                        	if x['@type']=='sequence variant':
                                 	j=j+1
                                 	Seq_Var_Dict['Sequence Varient '+str(j)]=x['original']+' Turns to '+x['variation']+'at position: '+ x['location']['position']['@position']
			print "\nVariations Of " +self.accession[i] + ":\n"
			i=i+1
                	print(json.dumps(Seq_Var_Dict, indent=4, sort_keys=True))
	# this function prints out all the information for each accession number
	def PrintAll(self):	
		
		for i in range(len(self.accession)):
			print "\nInformation for accession number: "+ self.accession[i]
			
			#gene name
			if isinstance(self.entry[i]['uniprot']['entry']['gene']['name'],list):
                               	print "\nGene Name: "  + self.entry[i]['uniprot']['entry']['gene']['name'][0]['#text']
                        else:
                                print "\nGene Name: "+ self.entry[i]['uniprot']['entry']['gene']['name']['#text']
			#title
			print "\nTitle: "  + self.entry[i]['uniprot']['entry']['reference'][0]['citation']['title']

			#protein
                        print "\nProtein Name: " + self.entry[i]['uniprot']['entry']['protein']['recommendedName']['fullName']

			#organism
		        print "\nOrganism: " + self.entry[i]['uniprot']['entry']['organism']['name'][0]['#text']

			#protein sequence
			print "\nProtein Sequence: "+ "\n" + self.entry[i]['uniprot']['entry']['sequence']['#text']
			a=0
			Mod_Dict={}
			for x in self.entry[i]['uniprot']['entry']['feature']:
                                if x['@type']=='modified residue':
                                        a=a+1
                                        Mod_Dict['Modification number '+str(a)]='Description= '+x['@description']
                        print "\nModified Genes: " + "\n"
			if len(Mod_Dict)==0:
                                print "\nThere are no modified genes"
                        else:
                                print(json.dumps(Mod_Dict, indent=4, sort_keys=True))
			b=0
			Seq_Var_Dict={}
                        for x in self.entry[i]['uniprot']['entry']['feature']:
                                if x['@type']=='sequence variant':
                                        b=b+1
                                        Seq_Var_Dict['Sequence Varient '+str(b)]=x['original']+' Turns to '+x['variation']+'at position: '+ x['location']['position']['@position']
                        print "\nVariations: " + "\n"
                        print(json.dumps(Seq_Var_Dict, indent=4, sort_keys=True))
