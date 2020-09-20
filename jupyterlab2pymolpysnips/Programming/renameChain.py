"""
cmd.do('alter ${1:3fa0} and chain ${2:A}, chain=${3:"C"};')
cmd.do('sort;')
"""
cmd.do('alter 3fa0 and chain A, chain="C";')
cmd.do('sort;')

# Description:  Rename a chain. 
# Source:  https://www.pymolwiki.org/index.php/Sync

