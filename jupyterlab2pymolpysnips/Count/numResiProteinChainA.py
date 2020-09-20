"""
cmd.do('sel = 'chain A and polymer.protein'; print(len(set([(i.chain, i.resi, i.resn) for i in cmd.get_model(sel).atom])));')
"""
cmd.do('sel = 'chain A and polymer.protein'; print(len(set([(i.chain, i.resi, i.resn) for i in cmd.get_model(sel).atom])));')

# Description:  Print the number of residues in chain A of a protein.
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15387.html

