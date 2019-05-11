import os
import pandas as pd

with open ("F:/FINAL PROJECT/GROMIHA DATASET/PDB FILES/HIGH/1atn.pdb") as data:
	p= list(data)

n= []
l=[]
t=[]
for m in p:
	k = m.split()
	if k[0] == 'HELIX': 
		print(k)
