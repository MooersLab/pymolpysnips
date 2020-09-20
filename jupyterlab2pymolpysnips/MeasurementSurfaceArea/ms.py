"""
cmd.do('fetch ${1:3nd3},name=${1:3nd3}, type=pdb, async=0')
cmd.do('select ${2:temp}, ${3:3nd3} and chain A;')
cmd.do('run ${3:/Users/blaine-mooers/Scripts/PyMOLScripts/msms_pymol.py};')
cmd.do('calc_msms_area ${2:temp};')
"""
cmd.do('fetch 3nd3,name=3nd3, type=pdb, async=0')
cmd.do('select temp, 3nd3 and chain A;')
cmd.do('run /Users/blaine-mooers/Scripts/PyMOLScripts/msms_pymol.py;')
cmd.do('calc_msms_area temp;')

# Description:  Measure surface area. 
# Source:  placeHolder

