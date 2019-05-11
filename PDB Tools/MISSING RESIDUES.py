import os
import pandas as pd

with open ("F:/FINAL PROJECT/GROMIHA DATASET/PDB FILES/HIGH/1ATN.pdb") as data:
	p= list(data)

n= []
l=[]
t=[]
for m in p:
	k = m.split()
	if k[0] == 'REMARK': 
		if k[1] == '465':
			print(k)
