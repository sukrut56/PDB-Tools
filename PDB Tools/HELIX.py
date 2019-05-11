import os

with open ("F:/.pdb") as data:
	p= list(data)

for m in p:
	k = m.split()
	if k[0] == 'HELIX': 
		print(k)
