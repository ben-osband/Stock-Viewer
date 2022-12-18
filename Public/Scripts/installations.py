# Benjamin Osband
# 12/18/2022
# installations.py
# runs pip commands as subprocesses to make sure pip is upgraded to
# the latest version and installs all necessary packages and modules

import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PySimpleGUI'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yahoo-finance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime'])