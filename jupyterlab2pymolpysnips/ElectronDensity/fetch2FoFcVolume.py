"""
cmd.do('fetch ${1:3nd4}, type=2fofc, async=0;')
cmd.do('volume 2fofcmap, ${1:3nd4}_2fofc, 1, ${2:LongGlycan}, carve = 1.8;')
"""
cmd.do('fetch 3nd4, type=2fofc, async=0;')
cmd.do('volume 2fofcmap, 3nd4_2fofc, 1, LongGlycan, carve = 1.8;')

# Description:  Fetch 2FoFc map as a volume.
# Source:  placeHolder

