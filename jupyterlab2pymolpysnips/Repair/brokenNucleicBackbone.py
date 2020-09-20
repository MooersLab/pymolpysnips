"""
cmd.do('[cmd.bond(f"/5fur//E/{i}/O3'", f"/5fur//E/{i+1}/P") for i in range(${1:1}, ${2:80})]; ')
cmd.do('[cmd.bond(f"/5fur//F/{i}/O3'", f"/5fur//F/{i+1}/P") for i in range(${3:81}, ${3:160})];')
"""
cmd.do('[cmd.bond(f"/5fur//E/{i/O3'", f"/5fur//E/{i+1/P") for i in range(1, 80)]; ')
cmd.do('[cmd.bond(f"/5fur//F/{i/O3'", f"/5fur//F/{i+1/P") for i in range(81, 160)];')

# Description:  Create bonds between phosphorous and O3* atoms in a low resolution DNA structure that is 80 base pairs long.
# Source:  https://www.mail-archive.com/pymol-users@lists.sourceforge.net/msg15658.html

