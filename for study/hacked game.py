from colorama import Fore
import random as rand
import shutil
import time as t
print(Fore.RED+"Error!Virus detected!")
print(Fore.GREEN+"",end="")
t.sleep(5)
while True:
    print("".join([str(rand.randint(0,1)) for i in range(shutil.get_terminal_size().columns)]))
