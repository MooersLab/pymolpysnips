"""
cmd.do('stereo walleye; ')
cmd.do('set ray_shadow, off; ')
cmd.do('#draw 3200,2000;')
cmd.do('draw ${1:1600,1000}; ')
cmd.do('png ${2:aaa}.png')
cmd.do('${0}')
"""
cmd.do('stereo walleye; ')
cmd.do('set ray_shadow, off; ')
cmd.do('#draw 3200,2000;')
cmd.do('draw 1600,1000; ')
cmd.do('png aaa.png')

# Description:  Stereo draw.
# Source:  placeHolder

