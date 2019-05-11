import os
import pandas as pd

with open ("F:/FINAL PROJECT/GROMIHA DATASET/PDB FILES/HIGH/1ATN.pdb") as data:
	p= list(data)

n= []
l=[]
t=[]
for t in p: 
	k= t.split()
	if k[0] == 'HETATM':
			print(k)
