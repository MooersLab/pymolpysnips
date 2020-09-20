"""
cmd.do('pseudoatom ${1:forLabel};')
cmd.do('label ${1:forLabel}, '%0';')
cmd.do('set label_color, ${2:red};')
"""
cmd.do('pseudoatom forLabel;')
cmd.do('label forLabel, '%0';')
cmd.do('set label_color, red;')

# Description:  Position label with pseudoatom. 
# Source:  placeHolder

