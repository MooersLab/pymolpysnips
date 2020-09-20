"""
cmd.do('stored.names = [];  iterate_state 1, (resi ${1:101}), stored.names.append([name]); ')
cmd.do('stored.coords = []; iterate_state 1, (resi ${1:101})), stored.coords.append([x,y,z]); ')
cmd.do('[print(i,j) for i,j in zip(stored.names, stored.coords)];')
"""
cmd.do('stored.names = [];  iterate_state 1, (resi 101), stored.names.append([name]); ')
cmd.do('stored.coords = []; iterate_state 1, (resi 101)), stored.coords.append([x,y,z]); ')
cmd.do('[print(i,j) for i,j in zip(stored.names, stored.coords)];')

# Description:  Print the atom names and coordinates of the atoms in a residue.
# Source:  https://www.pymolwiki.org/index.php/Sync

"""
cmd.do('stored.coords = []; iterate_state 1, (resi ${1:101}), stored.coords.append([x,y,z]); ')
cmd.do('stored.names = [];  iterate_state 1, (resi ${1:101}), stored.names.append([name]);')
cmd.do('stored.names3 = [tuple(i) for i in stored.names];')
cmd.do('[print(i,j) for i,j in(zip(stored.names3, stored.coords)];')
"""
cmd.do('stored.coords = []; iterate_state 1, (resi 101), stored.coords.append([x,y,z]); ')
cmd.do('stored.names = [];  iterate_state 1, (resi 101), stored.names.append([name]);')
cmd.do('stored.names3 = [tuple(i) for i in stored.names];')
cmd.do('[print(i,j) for i,j in(zip(stored.names3, stored.coords)];')

# Description:  Print the atom names as tuples and coordinates of the atoms in a residue as a list.
# Source:  https://www.pymolwiki.org/index.php/Sync

