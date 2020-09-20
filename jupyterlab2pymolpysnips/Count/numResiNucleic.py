"""
cmd.do('sel = 'polymer.nucleic'; print(len(set([(i.resi, i.resn) for i in cmd.get_model(sel).atom])));')
"""
cmd.do('sel = 'polymer.nucleic'; print(len(set([(i.resi, i.resn) for i in cmd.get_model(sel).atom])));')

# Description:  Print the number of residues in a nulceic acid (all chains).
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15387.html

