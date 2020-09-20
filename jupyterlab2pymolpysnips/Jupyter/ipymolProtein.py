"""
cmd.do('# Start pymol in terminal with pymol -R;')
cmd.do('# Select pymol.python as kernel in juptyer;')
cmd.do('from ipymol import viewer as ipv;')
cmd.do('ipv.start() # Start PyMOL RPC server;')
cmd.do('')
cmd.do('ipv.do('fetch 1lw9');')
cmd.do('ipv.do('rv');')
cmd.do('# The double parentheses are required when set_view is run this way.;')
cmd.do('ipv.set_view((-0.13,-0.4,-0.91,0.89,-0.45,0.07,-0.44,-0.8,0.41,0.0,0.0,-182.47,35.13,11.48,9.72,149.64,215.3,-20.0));')
cmd.do('ipv.do('AOD');')
cmd.do('ipv.png('testipymolT4L.png');')
"""
cmd.do('# Start pymol in terminal with pymol -R;')
cmd.do('# Select pymol.python as kernel in juptyer;')
cmd.do('from ipymol import viewer as ipv;')
cmd.do('ipv.start() # Start PyMOL RPC server;')
cmd.do('')
cmd.do('ipv.do('fetch 1lw9');')
cmd.do('ipv.do('rv');')
cmd.do('# The double parentheses are required when set_view is run this way.;')
cmd.do('ipv.set_view((-0.13,-0.4,-0.91,0.89,-0.45,0.07,-0.44,-0.8,0.41,0.0,0.0,-182.47,35.13,11.48,9.72,149.64,215.3,-20.0));')
cmd.do('ipv.do('AOD');')
cmd.do('ipv.png('testipymolT4L.png');')

# Description:  Demo of the use of the RPC server with a protein via ipymol.
# Source:  placeHolder

