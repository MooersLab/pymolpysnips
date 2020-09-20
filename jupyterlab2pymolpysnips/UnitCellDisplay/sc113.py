"""
cmd.do('run $HOME/${1:Scripts/PyMOLscripts/supercell.py};')
cmd.do('supercell 1, 1, 1, ,  ${2:orange},  ${3:supercell1}, 1;')
"""
cmd.do('run $HOME/Scripts/PyMOLscripts/supercell.py;')
cmd.do('supercell 1, 1, 1, ,  orange,  supercell1, 1;')

# Description:  Display all symmetry mates in three unit cels along c. Uses supercell.py in $HOME/Scripts/PyMOLscripts/.
# Source:  placeHolder

