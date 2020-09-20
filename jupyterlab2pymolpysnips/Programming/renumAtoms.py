"""
cmd.do('alter {$1:3fa0}, ID=ID+${2:100};')
cmd.do('sort;')
"""
cmd.do('alter {$1:3fa0, ID=ID+100;')
cmd.do('sort;')

# Description:  Add or substract a atom number offset.
# Source:  https://www.pymolwiki.org/index.php/Sync

