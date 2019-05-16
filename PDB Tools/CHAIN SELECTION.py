import os

with open ("F:/.pdb") as data:
	p= list(data)

t=[]
for t in p: 
	k= t.split()
	if k[0] == 'ATOM':
		if k[4] == 'A':
			print(k)

with open("example.pdb", "w") as f:
	for u in t:
		f.writelines(u)
f.close()
