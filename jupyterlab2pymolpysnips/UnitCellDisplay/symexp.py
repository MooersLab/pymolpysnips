"""
cmd.do('symexp ${1:symm}, ${2:3fa0}, (${2:3fa0}), ${3:20},${4:1};')
"""
cmd.do('symexp symm, 3fa0, (3fa0), 20,1;')

# Description:  The code expands the asymmetric unit. It like the generate symmetry mates command but it provides more control over the prefix name of the symmetry mates and the addition of unique segment identifiers for each symmetry mate. The usage: symexp prefix, object, (selection), cutoff, segidFlag. The cutoff is in Angstroms. The segidFlag set to 1 will add unique segids. For related functions, see SC***.
# Source:  https://www.pymolwiki.org/index.php/Symexp

