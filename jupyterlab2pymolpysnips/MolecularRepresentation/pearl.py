"""
cmd.do('create ${1:sodium2}, ${2:sodium1};')
cmd.do('set sphere_transparency, 0.4, ${1:sodium2};')
cmd.do('set sphere_scale, 1.05, ${1:sodium2};')
cmd.do('ray;')
"""
cmd.do('create sodium2, sodium1;')
cmd.do('set sphere_transparency, 0.4, sodium2;')
cmd.do('set sphere_scale, 1.05, sodium2;')
cmd.do('ray;')

# Description:  The pearl effect is made with two spheres with the outer sphere being transparent.
# Source:  placeHolder

