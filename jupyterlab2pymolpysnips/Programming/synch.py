"""
cmd.do('cmd.sync(timeout=${1:1.0},poll=${2:0.05});')
"""
cmd.do('cmd.sync(timeout=1.0,poll=0.05);')

# Description:  Wait unitl all current commands have been executed. A timeout ensures that that command ecentually returns.
# Source:  https://www.pymolwiki.org/index.php/Sync

