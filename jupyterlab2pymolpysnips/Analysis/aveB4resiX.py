"""
cmd.do('""""AveBResiX, prints the resiude number and the average bfactor. ')
cmd.do('Uses reduce and lambda, builtin Python functional porgramming functions. ')
cmd.do('Note that you need to convert the length of the list of Bfactors from an integer to a float before division into the sum. ')
cmd.do('"""')
cmd.do('Bfactors = [];')
cmd.do('iterate (resi ${1:133}), Bfactors.append(b);')
cmd.do('print( "Average B-factor of residue ", %{1:133} , "   = ", "%.2f" %(reduce(lambda x, y: x + y, Bfactors) / float(len(Bfactors))) )')
"""
cmd.do('""""AveBResiX, prints the resiude number and the average bfactor. ')
cmd.do('Uses reduce and lambda, builtin Python functional porgramming functions. ')
cmd.do('Note that you need to convert the length of the list of Bfactors from an integer to a float before division into the sum. ')
cmd.do('"""')
cmd.do('Bfactors = [];')
cmd.do('iterate (resi 133), Bfactors.append(b);')
cmd.do('print( "Average B-factor of residue ", %{1:133 , "   = ", "%.2f" %(reduce(lambda x, y: x + y, Bfactors) / float(len(Bfactors))) )')

# Description:  AveBResiX, prints the resiude number and the average bfactor. 
# Source:  placeHolder

