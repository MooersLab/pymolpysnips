"""
cmd.do('iterate (resi ${1:101}), print(name + " %.2f" % vdw);')
"""
cmd.do('iterate (resi 101), print(name + " %.2f" % vdw);')

# Description:  Print the van Der Waals radii of the atoms in of a residue.
# Source:  https://www.pymolwiki.org/index.php/Sync

