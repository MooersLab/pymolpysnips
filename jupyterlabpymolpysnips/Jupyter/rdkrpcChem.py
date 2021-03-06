cmd.do('import os;')
cmd.do('import rdkit;')
cmd.do('from rdkit import Chem;')
cmd.do('from rdkit.Chem import AllChem;')
cmd.do('from rdkit.Chem import PyMol;')
cmd.do('')
cmd.do('s = PyMOL.MolViewer();')
cmd.do('mol = Chem.MolFromSmiles \')
cmd.do('   ('CCOCCn1c(C2CC[NH+](CCc3ccc(C(C)(C)C(=O)[O-])cc3)CC2)nc2ccccc21');')
cmd.do('mol = AllChem.AddHs(mol);')
cmd.do('AllChem.EmbedMolecule(mol);')
cmd.do('AllChem.MMFFOptimizeMolecule(mol);')
cmd.do('s.ShowMol(mol, name = 'bilastine', showOnly = False);')
cmd.do('s.Zoom('bilastine');')
cmd.do('s.SetDisplayStyle('bilastine', 'sticks');')
cmd.do('s.GetPNG(preDelay=5);')
