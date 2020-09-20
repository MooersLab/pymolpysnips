"""
cmd.do('To load a bunch of related files from inside PyMOL all at once:')
cmd.do('')
cmd.do('run loadFiles.py')
cmd.do('loadFiles refine_*.pdb')
cmd.do('')
cmd.do('')
cmd.do('To align all of the loaded RNA structures in all possible combinations by their C1' carbon atoms:')
cmd.do('')
cmd.do('run optAlignRNA.py')
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()]')
cmd.do('')
cmd.do('(Yes, that construct is a list comprehension inside a list comprehension!)')
cmd.do('')
cmd.do('To save a multiple models in a file to separate pdb files,')
cmd.do('')
cmd.do('run saveSep.py')
cmd.do('saveSep ')
cmd.do('or ')
cmd.do('saveSep prefix')
"""
cmd.do('To load a bunch of related files from inside PyMOL all at once:')
cmd.do('')
cmd.do('run loadFiles.py')
cmd.do('loadFiles refine_*.pdb')
cmd.do('')
cmd.do('')
cmd.do('To align all of the loaded RNA structures in all possible combinations by their C1' carbon atoms:')
cmd.do('')
cmd.do('run optAlignRNA.py')
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()]')
cmd.do('')
cmd.do('(Yes, that construct is a list comprehension inside a list comprehension!)')
cmd.do('')
cmd.do('To save a multiple models in a file to separate pdb files,')
cmd.do('')
cmd.do('run saveSep.py')
cmd.do('saveSep ')
cmd.do('or ')
cmd.do('saveSep prefix')

# Description:  These are the instructions for loading and aligning multiple files.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

