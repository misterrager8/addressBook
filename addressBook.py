from util import viewUnix
import sys
import subprocess
import os

if __name__ == "__main__":
  if (sys.argv[1] == "dt"):
    path = os.getcwd() + "/util"
    os.chdir(path)
    subprocess.call("/Users/chemlleijoseph/jython2.7.1/bin/jython viewDesktop.py", shell = True)
  elif (sys.argv[1] == "cl"):
    viewUnix.mainMenu()