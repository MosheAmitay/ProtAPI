import os,sys

fname=raw_input("enter name of text file with accession numbers:  ")
with open(fname,'r') as a:
    accs=a.read().split("\n")
print accs
platforms=[]
for a in accs:
	if "GSE" in a:
		url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+a
		os.system("wget -O "+a+" "+url)
		with open(a,'r') as f:
    			lines = f.read().split("\n")
	
		i=0
		for line in lines:
        		if "Platforms" in line:
        	        	break
		        i=i+1
		i=i+1
		j=1
		flag=1
		while(flag==1):
		        if "valign" in lines[i]:
        		        if j>1:
        	        	        platform=lines[i]
        	                	flag=0
		                else: j=j+1
		        i=i+1
		platforms.append(platform.split(">")[1].split("<")[0])
		os.remove(a)
with open('output.txt', 'w') as f:
    for item in platforms:
        f.write("%s\n" % item)
print("the results are in output.txt")
