"""
cmd.do('# Copyright (c) 2004 Robert L. Campbell')
cmd.do('#')
cmd.do('# Modified for use with Python3.')
cmd.do('# Jan. 29, 2020 ')
cmd.do('# Blaine Mooers, PhD')
cmd.do('# Univ. of Oklahoma Health Sciences Center')
cmd.do('#')
cmd.do('#')
cmd.do('from pymol import cmd')
cmd.do('import glob')
cmd.do('')
cmd.do('def loadFiles(files):')
cmd.do('  """')
cmd.do('  load_files <files>')
cmd.do('')
cmd.do('  loads multiple files (using filename globbing)')
cmd.do('  into a multiple objects named as the files are (e.g. collection of')
cmd.do('  downloaded PDB files).')
cmd.do('')
cmd.do('  e.g. load_files prot_*.pdb')
cmd.do('  """')
cmd.do('  file_list = glob.glob(files)')
cmd.do('  if file_list:')
cmd.do('    file_list.sort()')
cmd.do('    for i in file_list:')
cmd.do('      #obj_name = i.replace('.pdb','')')
cmd.do('      #cmd.load(file_list[i],obj_name)')
cmd.do('      cmd.load(i)')
cmd.do('  else:')
cmd.do('    print("No files found for pattern %s" % files)')
cmd.do('')
cmd.do('cmd.extend('loadFiles',loadFiles)')
"""
cmd.do('# Copyright (c) 2004 Robert L. Campbell')
cmd.do('#')
cmd.do('# Modified for use with Python3.')
cmd.do('# Jan. 29, 2020 ')
cmd.do('# Blaine Mooers, PhD')
cmd.do('# Univ. of Oklahoma Health Sciences Center')
cmd.do('#')
cmd.do('#')
cmd.do('from pymol import cmd')
cmd.do('import glob')
cmd.do('')
cmd.do('def loadFiles(files):')
cmd.do('  """')
cmd.do('  load_files <files>')
cmd.do('')
cmd.do('  loads multiple files (using filename globbing)')
cmd.do('  into a multiple objects named as the files are (e.g. collection of')
cmd.do('  downloaded PDB files).')
cmd.do('')
cmd.do('  e.g. load_files prot_*.pdb')
cmd.do('  """')
cmd.do('  file_list = glob.glob(files)')
cmd.do('  if file_list:')
cmd.do('    file_list.sort()')
cmd.do('    for i in file_list:')
cmd.do('      #obj_name = i.replace('.pdb','')')
cmd.do('      #cmd.load(file_list[i],obj_name)')
cmd.do('      cmd.load(i)')
cmd.do('  else:')
cmd.do('    print("No files found for pattern %s" % files)')
cmd.do('')
cmd.do('cmd.extend('loadFiles',loadFiles)')

# Description:  Load into PyMOL multiple files with a common file stem. The is a script by Robert Campbell that updated for Python3.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.
