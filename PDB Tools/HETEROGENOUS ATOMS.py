import os

with open ("F:/.pdb") as data:
	p= list(data)

t=[]
for t in p: 
	k= t.split()
	if k[0] == 'HETATM':

with open("example.pdb", "w") as f:
	for u in t:
		f.writelines(k)
f.close()
