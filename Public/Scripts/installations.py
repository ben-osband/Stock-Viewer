import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PySimpleGUI'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yahoo-finance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime'])