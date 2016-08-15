#Main method

import io
import sys
import subprocess

history = subprocess.check_output(['wc', '-l', '/root/.bash_history'])

if history[0] > 1:
	print 'There is history'
else:
	print 'There is no history'
