"""
cmd.do('def rvj(StoredView=0, decimal_places=2, outname="roundedview.txt"):')
cmd.do('    """')
cmd.do('    rvj() is a modification of the the rv() function (aka the roundview.py) ')
cmd.do('    so that it can run in Jupyter notebooks with the ipymol.viewer. ')
cmd.do('    A set_view string is printed to the noteobook in a format that is ready ')
cmd.do('    for reuse. ')
cmd.do('    ')
cmd.do('    The ipymol module was developed by Carlos Hernandez:')
cmd.do('    ')
cmd.do('    https://github.com/cxhernandez/ipymol')
cmd.do('    ')
cmd.do('    The pre-requisites for installing ipymol are as follows:')
cmd.do('    ')
cmd.do('    1. Make a jupyter notebook kernel for Python interpreter inside of ')
cmd.do('       the Schrodinger PyMOL. See the PyMOL Snippets GitHub Page for ')
cmd.do('       a description of how to make one.')
cmd.do('    2. Install the following build of ipymol at the PyMOL prompt.')
cmd.do('       You need to log into your GitHub account first.')
cmd.do('    ')
cmd.do('    pip install git+pip install git+https://github.com/cxhernandez/ipymol.git@2a30d6ec1588434e6f0f72a1d572444f89ff535b')
cmd.do('    ')
cmd.do('    3. Make a bash alias to this PyMOL app file.')
cmd.do('    ')
cmd.do('    4. Launch the jupyter notebook and select the pymol.python kernel.')
cmd.do('    ')
cmd.do('    5. Open a terminal instance from the File pulldown in jupyter notebook.')
cmd.do('    ')
cmd.do('    6. Enter `pymol -Rq` to launch an interactive instance of PyMOL.')
cmd.do('    ')
cmd.do('    7. Enter the following code to load ipymol and conmect to PyMOL')
cmd.do('    ')
cmd.do('    from ipymol import viewer as ipv')
cmd.do('    ipv.start()   # Start PyMOL RPC server')
cmd.do('    ')
cmd.do('    Now you can change the scene manually and send the display as static ')
cmd.do('    image to a cell in the jupyter notebook.')
cmd.do('    ')
cmd.do('    It is assumed that the viewer class of the ipymol moduel has been ')
cmd.do('    imported as ipv. ')
cmd.do('    ')
cmd.do('    I made the following modifications of roundview.py.')
cmd.do('    The cmd.get_view was replaced with ipv.get_view.')
cmd.do('    The cmd.extend was replaced with ipv.extend.')
cmd.do('    The myRoundedList was returned for further processing.')
cmd.do('    ')
cmd.do('    MIT License')
cmd.do('    ')
cmd.do('    Copyright:')
cmd.do('    Blaine Mooers and the OU Board of Regents')
cmd.do('    Uniersity of Oklahoma Health Sciences Center')
cmd.do('    Oklahoma City, OK 73104')
cmd.do('    ')
cmd.do('    29 April 2020')
cmd.do('    ')
cmd.do('    """')
cmd.do('    ')
cmd.do(' ')
cmd.do('    StoredView = int(StoredView)')
cmd.do('    decimal_places = int(decimal_places)')
cmd.do(' ')
cmd.do('    #call the get_view function')
cmd.do(' ')
cmd.do('    m = ipv.get_view(StoredView)')
cmd.do(' ')
cmd.do(' ')
cmd.do('    #Make a list of the elements in the orientation matrix.')
cmd.do(' ')
cmd.do('    myList = [m[0], m[1], m[2], m[3], m[4], m[5], m[6],m[7], m[8], m[9],')
cmd.do('              m[10], m[11], m[12], m[13], m[14],m[15], m[16], m[17]]')
cmd.do(' ')
cmd.do('    #Round off the matrix elements to two decimal places (two fractional places)')
cmd.do('    #This rounding approach solved the problem of unwanted')
cmd.do('    #whitespaces when I tried to use a string format statement')
cmd.do(' ')
cmd.do('    myRoundedList = [round(elem, decimal_places) for elem in myList]')
cmd.do('    ')
cmd.do('    #x is the string template for the output. The whitespace is required')
cmd.do('    #between the "set_view" and "("')
cmd.do(' ')
cmd.do('    x = 'set_view ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17});'')
cmd.do(' ')
cmd.do('    # Print to the command history window.')
cmd.do('    print(x.format(*myRoundedList))')
cmd.do(' ')
cmd.do('    #Write to a text file.')
cmd.do('    myFile = open("roundedview.txt", "a")')
cmd.do('    myFile.write(x.format(*myRoundedList) + "")')
cmd.do('    myFile.close()')
cmd.do('    return myRoundedList')
cmd.do('ipv.extend("rv", rv)')
"""
cmd.do('def rvj(StoredView=0, decimal_places=2, outname="roundedview.txt"):')
cmd.do('    """')
cmd.do('    rvj() is a modification of the the rv() function (aka the roundview.py) ')
cmd.do('    so that it can run in Jupyter notebooks with the ipymol.viewer. ')
cmd.do('    A set_view string is printed to the noteobook in a format that is ready ')
cmd.do('    for reuse. ')
cmd.do('    ')
cmd.do('    The ipymol module was developed by Carlos Hernandez:')
cmd.do('    ')
cmd.do('    https://github.com/cxhernandez/ipymol')
cmd.do('    ')
cmd.do('    The pre-requisites for installing ipymol are as follows:')
cmd.do('    ')
cmd.do('    1. Make a jupyter notebook kernel for Python interpreter inside of ')
cmd.do('       the Schrodinger PyMOL. See the PyMOL Snippets GitHub Page for ')
cmd.do('       a description of how to make one.')
cmd.do('    2. Install the following build of ipymol at the PyMOL prompt.')
cmd.do('       You need to log into your GitHub account first.')
cmd.do('    ')
cmd.do('    pip install git+pip install git+https://github.com/cxhernandez/ipymol.git@2a30d6ec1588434e6f0f72a1d572444f89ff535b')
cmd.do('    ')
cmd.do('    3. Make a bash alias to this PyMOL app file.')
cmd.do('    ')
cmd.do('    4. Launch the jupyter notebook and select the pymol.python kernel.')
cmd.do('    ')
cmd.do('    5. Open a terminal instance from the File pulldown in jupyter notebook.')
cmd.do('    ')
cmd.do('    6. Enter `pymol -Rq` to launch an interactive instance of PyMOL.')
cmd.do('    ')
cmd.do('    7. Enter the following code to load ipymol and conmect to PyMOL')
cmd.do('    ')
cmd.do('    from ipymol import viewer as ipv')
cmd.do('    ipv.start()   # Start PyMOL RPC server')
cmd.do('    ')
cmd.do('    Now you can change the scene manually and send the display as static ')
cmd.do('    image to a cell in the jupyter notebook.')
cmd.do('    ')
cmd.do('    It is assumed that the viewer class of the ipymol moduel has been ')
cmd.do('    imported as ipv. ')
cmd.do('    ')
cmd.do('    I made the following modifications of roundview.py.')
cmd.do('    The cmd.get_view was replaced with ipv.get_view.')
cmd.do('    The cmd.extend was replaced with ipv.extend.')
cmd.do('    The myRoundedList was returned for further processing.')
cmd.do('    ')
cmd.do('    MIT License')
cmd.do('    ')
cmd.do('    Copyright:')
cmd.do('    Blaine Mooers and the OU Board of Regents')
cmd.do('    Uniersity of Oklahoma Health Sciences Center')
cmd.do('    Oklahoma City, OK 73104')
cmd.do('    ')
cmd.do('    29 April 2020')
cmd.do('    ')
cmd.do('    """')
cmd.do('    ')
cmd.do(' ')
cmd.do('    StoredView = int(StoredView)')
cmd.do('    decimal_places = int(decimal_places)')
cmd.do(' ')
cmd.do('    #call the get_view function')
cmd.do(' ')
cmd.do('    m = ipv.get_view(StoredView)')
cmd.do(' ')
cmd.do(' ')
cmd.do('    #Make a list of the elements in the orientation matrix.')
cmd.do(' ')
cmd.do('    myList = [m[0], m[1], m[2], m[3], m[4], m[5], m[6],m[7], m[8], m[9],')
cmd.do('              m[10], m[11], m[12], m[13], m[14],m[15], m[16], m[17]]')
cmd.do(' ')
cmd.do('    #Round off the matrix elements to two decimal places (two fractional places)')
cmd.do('    #This rounding approach solved the problem of unwanted')
cmd.do('    #whitespaces when I tried to use a string format statement')
cmd.do(' ')
cmd.do('    myRoundedList = [round(elem, decimal_places) for elem in myList]')
cmd.do('    ')
cmd.do('    #x is the string template for the output. The whitespace is required')
cmd.do('    #between the "set_view" and "("')
cmd.do(' ')
cmd.do('    x = 'set_view ({0,{1,{2,{3,{4,{5,{6,{7,{8,{9,{10,{11,{12,{13,{14,{15,{16,{17);'')
cmd.do(' ')
cmd.do('    # Print to the command history window.')
cmd.do('    print(x.format(*myRoundedList))')
cmd.do(' ')
cmd.do('    #Write to a text file.')
cmd.do('    myFile = open("roundedview.txt", "a")')
cmd.do('    myFile.write(x.format(*myRoundedList) + "")')
cmd.do('    myFile.close()')
cmd.do('    return myRoundedList')
cmd.do('ipv.extend("rv", rv)')

# Description:  Return settings in rounded format while running PyMOL via the RCP server ipymol in a jupuyter notebook. This is a modified version of the roundview.py script.
# Source:  placeHolder

