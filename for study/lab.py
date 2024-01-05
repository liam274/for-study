import getpass
import time
print(getpass.getpass("password:"))
print("Yo"+"\u0332")
time.sleep(10)
b=[]
with open("english\\spelling_check_term2_1.txt","r") as file:
    a=file.readlines()[0]
    print(a)
    b.append(a)
    b="&".join(b)
    print(b)
