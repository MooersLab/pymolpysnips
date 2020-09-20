"""
cmd.do('alter ${1:3fa0}, resi=str(int(resi)+${2:100});sort;')
"""
cmd.do('alter 3fa0, resi=str(int(resi)+100);sort;')

# Description:  Add or substract a residue number offset.
# Source:  https://www.pymolwiki.org/index.php/Sync

