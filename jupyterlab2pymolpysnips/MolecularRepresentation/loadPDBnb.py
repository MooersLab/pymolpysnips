"""
cmd.do('fetch ${1:3nd3},name=${1:3nd3}, type=pdb, async=0;')
cmd.do('orient;')
cmd.do('set stick_radius, ${2:1.2};')
cmd.do('hide (name H*);')
cmd.do('set nb_sphere_size, ${3:0.35};')
cmd.do('set nb_spheres_quality, ${4:1};')
cmd.do('show nb_spheres;')
"""
cmd.do('fetch 3nd3,name=3nd3, type=pdb, async=0;')
cmd.do('orient;')
cmd.do('set stick_radius, 1.2;')
cmd.do('hide (name H*);')
cmd.do('set nb_sphere_size, 0.35;')
cmd.do('set nb_spheres_quality, 1;')
cmd.do('show nb_spheres;')

# Description:  Load PDB nb spheres. 
# Source:  placeHolder

