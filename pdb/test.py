from YNpdb import *

ids = ['6QCW']
colmns = ['chainLength','ligandId']
dict_1 = YNpdb.search_pdb(ids, colmns) #checks the first function
dict_2 = YNpdb.print_all(ids, colmns) #checks the second function
