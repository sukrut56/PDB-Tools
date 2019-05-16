# PDB-Tools
You can find various tools required to analyze the PDB structure. 

All you need to do is edit the file location column so that the code can read your file path. 
I will be adding more features and also will try to save the selected feature in PDB format.  

To save the edited file in PDB format, use this code: 

with open("example.pdb", "w") as f:
	for u in t:
	f.writelines(p)
f.close()
