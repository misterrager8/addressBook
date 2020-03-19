from util import viewUnix
import sys
import subprocess
import os

#TEST DATA
#personArray = []
#personArray.append(person("john", "smith", "1-28-2020", "jsmith@gmail.com", "404-772-7998"))
#personArray.append(person("jane", "jones", "5-7-2020", "jjones@gmail.com", "404-772-1234"))
#personArray.append(person("roger", "joseph", "1-3-2020", "rjoseph@gmail.com", "404-772-5678"))
#personArray.append(person("timothy", "samuels", "8-1-2020", "tsamuels@gmail.com", "404-772-4532"))
#personArray.append(person("karen", "edwards", "6-18-2020", "kedwards@gmail.com", "404-772-4384"))
#personArray.append(person("vanessa", "thompson", "11-12-2020", "vthompson@gmail.com", "404-772-3029"))

if __name__ == "__main__":
  if (sys.argv[1] == "dt"):
    path = os.getcwd() + "/util"
    os.chdir(path)
    subprocess.call("/Users/chemlleijoseph/jython2.7.1/bin/jython viewDesktop.py", shell = True)
  elif (sys.argv[1] == "cl"):
    viewUnix.mainMenu()