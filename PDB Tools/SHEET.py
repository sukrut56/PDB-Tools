import os

with open ("F:/.pdb") as data:
	p= list(data)

for t in p: 
	k= t.split()
	if k[0] == 'SHEET': 
		print(k)
