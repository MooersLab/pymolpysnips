"""
cmd.do('fetch ${1:3nd4}_2fofc, type=2fofc, async=0;')
cmd.do('isosurface 2fofcmap, ${1:3nd4}_2fofc, 1, ${2:LongGlycan}, carve = 1.8;')
"""
cmd.do('fetch 3nd4_2fofc, type=2fofc, async=0;')
cmd.do('isosurface 2fofcmap, 3nd4_2fofc, 1, LongGlycan, carve = 1.8;')

# Description:  Fetch 2FoFc map as an isosurface.
# Source:  placeHolder

