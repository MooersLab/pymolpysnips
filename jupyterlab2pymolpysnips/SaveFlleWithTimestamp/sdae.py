"""
cmd.do('python;')
cmd.do('import datetime;')
cmd.do('from pymol import cmd; ')
cmd.do('DT =datetime.datetime.now().strftime("yr%Ymo%mday%dhr%Hmin%M");')
cmd.do('s = str(DT); ')
cmd.do('cmd.save(stemName+s+".dae"); ')
cmd.do('end python;')
"""
cmd.do('python;')
cmd.do('import datetime;')
cmd.do('from pymol import cmd; ')
cmd.do('DT =datetime.datetime.now().strftime("yr%Ymo%mday%dhr%Hmin%M");')
cmd.do('s = str(DT); ')
cmd.do('cmd.save(stemName+s+".dae"); ')
cmd.do('end python;')

# Description:  Save dae flle with timestamp
# Source:  placeHolder

