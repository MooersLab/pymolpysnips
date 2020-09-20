"""
cmd.do('[[${1:optAlignRNA}(x, y) for x in cmd.get_names()] for y in cmd.get_names()]')
"""
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()]')

# Description:  This is a two-fold nested list comprehension for any all parwise operation on the currently loaded objects. Replace optAlginRNA with any other function that operations on a pair of structrures.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

