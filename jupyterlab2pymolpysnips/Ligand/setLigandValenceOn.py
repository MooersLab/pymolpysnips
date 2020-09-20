"""
cmd.do('#Set on the valence of the ligand only')
cmd.do('set valence, on, resn ${1:RZS}; set valence, off, not resn ${2:RZS}')
"""
cmd.do('#Set on the valence of the ligand only')
cmd.do('set valence, on, resn RZS; set valence, off, not resn RZS')

# Description:  Turn on the ligand valence.
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15668.html

