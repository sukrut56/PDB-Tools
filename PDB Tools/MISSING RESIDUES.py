import os

with open ("F:/.pdb") as data:
	p= list(data)
	
for m in p:
	k = m.split()
	if k[0] == 'REMARK': 
		if k[1] == '465':
			

with open("example.pdb", "w") as f:
	for u in t:
		f.writelines(u)
f.close()
