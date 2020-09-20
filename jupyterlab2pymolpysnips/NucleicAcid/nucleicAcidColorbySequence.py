"""
cmd.do('select rna_A, resn A;')
cmd.do('select rna_C, resn C;')
cmd.do('select rna_G, resn G;')
cmd.do('select rna_U, resn U;')
cmd.do('select dna_T, resn T;')
cmd.do('color ${1:yellow}, rna_A;')
cmd.do('color ${2:red}, rna_C; ')
cmd.do('color ${3:gray40}, rna_G;')
cmd.do('color ${4:palecyan}, rna_U;')
cmd.do('color ${5:brown}, dna_T;')
"""
cmd.do('select rna_A, resn A;')
cmd.do('select rna_C, resn C;')
cmd.do('select rna_G, resn G;')
cmd.do('select rna_U, resn U;')
cmd.do('select dna_T, resn T;')
cmd.do('color yellow, rna_A;')
cmd.do('color red, rna_C; ')
cmd.do('color gray40, rna_G;')
cmd.do('color palecyan, rna_U;')
cmd.do('color brown, dna_T;')

# Description:  This code colors by the nucleotides by base seqence. It can be applied to any nucleic acid. It could make a good shortcut.
# Source:  Generated while helping Miranda Adams at U of Saint Louis.

