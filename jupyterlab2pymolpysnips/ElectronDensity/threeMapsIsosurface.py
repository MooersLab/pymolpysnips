"""
cmd.do('load ${1:4dgr}.pdb')
cmd.do('# Make sure to rename map file so that ')
cmd.do('# the root filename differs from pdb root filename')
cmd.do('load ${1:4dgr}_2fofc.ccp4, 2fofc;')
cmd.do('load ${1:4dgr}_fofc.ccp4, fofc;')
cmd.do('select  ${2:glycan}, resid 200 or (resid 469:477);')
cmd.do('isosurface ${3:mesh1}, 2fofc, 1.0, ${2:glycan};')
cmd.do('color density, ${3:mesh1};')
cmd.do('isosurface  ${4:mesh2}, fofc, 3.0, ${2:glycan};')
cmd.do('color green, ${4:mesh2};')
cmd.do('isosurface  ${5:mesh3}, fofc, -3.0, ${2:glycan};')
cmd.do('color red, ${5:mesh3};')
"""
cmd.do('load 4dgr.pdb')
cmd.do('# Make sure to rename map file so that ')
cmd.do('# the root filename differs from pdb root filename')
cmd.do('load 4dgr_2fofc.ccp4, 2fofc;')
cmd.do('load 4dgr_fofc.ccp4, fofc;')
cmd.do('select  glycan, resid 200 or (resid 469:477);')
cmd.do('isosurface mesh1, 2fofc, 1.0, glycan;')
cmd.do('color density, mesh1;')
cmd.do('isosurface  mesh2, fofc, 3.0, glycan;')
cmd.do('color green, mesh2;')
cmd.do('isosurface  mesh3, fofc, -3.0, glycan;')
cmd.do('color red, mesh3;')

# Description:  Three electron density as isosurface. 
# Source:  placeHolder

