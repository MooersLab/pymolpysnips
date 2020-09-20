"""
cmd.do('python;')
cmd.do('from pymol import cmd;')
cmd.do('for i in range(1,21):')
cmd.do('     name = 'label%d' % i;')
cmd.do('     cmd.pseudoatom(name, label='label font id %d' % i, pos=(0,0,0));')
cmd.do('     cmd.set('label_font_id', i, name);')
cmd.do('cmd.set('label_size', 50);')
cmd.do('cmd.set('grid_mode');')
cmd.do('python end;')
"""
cmd.do('python;')
cmd.do('from pymol import cmd;')
cmd.do('for i in range(1,21):')
cmd.do('     name = 'label%d' % i;')
cmd.do('     cmd.pseudoatom(name, label='label font id %d' % i, pos=(0,0,0));')
cmd.do('     cmd.set('label_font_id', i, name);')
cmd.do('cmd.set('label_size', 50);')
cmd.do('cmd.set('grid_mode');')
cmd.do('python end;')

# Description:  Print to the screen as labels that 21 font ids in their corresponding fonts in a grid. Each label is an object and appears in the internal gui. You can turn on and off the display of specific fonts.
# Source:  Answer by Thomas Holder https://sourceforge.net/p/pymol/mailman/message/28828647/


