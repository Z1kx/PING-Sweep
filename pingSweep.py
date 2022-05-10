import subprocess
import os


FNULL = open(os.devnull, 'w')

for i in range(1,101):
    result = subprocess.call(['ping', "-c 1", "192.168.201."+str(i)], stdout=FNULL, stderr=subprocess.STDOUT) #Ping chaque adresse ip 1 seule fois et renvoie pas d'output

    #result = subprocess.call(['ping', "-c 1", "192.168.1."+str(i)])
    if result == 0:
          print("192.168.201."+str(i))
