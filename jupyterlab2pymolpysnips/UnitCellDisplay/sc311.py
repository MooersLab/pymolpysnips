"""
cmd.do('run $HOME/${1:Scripts/PyMOLscripts/supercell.py};')
cmd.do('supercell 1, 1, 1, ,  ${2:orange},  ${3:supercell1}, 1;')
"""
cmd.do('run $HOME/Scripts/PyMOLscripts/supercell.py;')
cmd.do('supercell 1, 1, 1, ,  orange,  supercell1, 1;')

# Description:  Display all symmetry mates three three unit cells along a. Uses supercell.py in $HOME/Scripts/PyMOLscripts/.
# Source:  placeHolder

