"""
cmd.do('set bg_rgb, white;')
cmd.do('hide everything, all;')
cmd.do('show cartoon, ${1:3nd3};')
cmd.do('set cartoon_sampling,1;')
cmd.do('set cartoon_tube_radius, 0.5;')
cmd.do('set cartoon_ladder_mode, 0;')
cmd.do('set cartoon_transparency, ${2:0.65};')
cmd.do('set stick_radius ${3:0.12};')
cmd.do('show sticks;')
cmd.do('hide sticks, element H;')
"""
cmd.do('set bg_rgb, white;')
cmd.do('hide everything, all;')
cmd.do('show cartoon, 3nd3;')
cmd.do('set cartoon_sampling,1;')
cmd.do('set cartoon_tube_radius, 0.5;')
cmd.do('set cartoon_ladder_mode, 0;')
cmd.do('set cartoon_transparency, 0.65;')
cmd.do('set stick_radius 0.12;')
cmd.do('show sticks;')
cmd.do('hide sticks, element H;')

# Description:  This code shows that cartoon backbone tube as 65% transparent. It hides the rungs of the cartoon. It shows all of the non-H atoms are sticks. The motivation is to have the cartoon highlight the backbone without dominanting the scene.
# Source:  Develop ab initio.

