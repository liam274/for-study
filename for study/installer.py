import os
import sys
import shutil
import threading
import subprocess as subpro
#var
no=["no","n","","nope","no way"]
commands={"help":"Help you to know what we have",
          "uninstall":"uninstall the application",
          "install <var>":"""The var can be:
          packages                   install packages need"""}
#function
def system(com):
    return subpro.run(com,capture_output=True)
#main
while True:
    command=input(f"{os.getcwd()}>")
    command=command.split() if command is not None else "continue"
    if command=="continue":
        continue
    if command[0].lower()=="help":
        for i in commands:
            print(i,"\n",commands[i],sep="")
    elif command[0].lower()=="uninstall":
        if input("Do you want to uninstall?") not in no:
            shutil.rmtree(os.getcwd())
    elif command[0].lower()=="install":
        if command[1].lower()=="packages":
            list_of_model=["socket","winshell","playsound","pyperclip","sympy","pynput","keyboard","getch","colorama","psutil","readchar","gtts",
                           "shortcut","selenium","win10toast","pillow","termcolor","webcolors"]#packages
            check=threading.Thread(target=lambda:print("Doing need process..."))
            check.start()
            check.join()
            if system("pip")==1:
                print("Deceted pip is not sucessfully installed in your computer...")
                print("Please type y later on during the process.")
                system("python -m pip uninstall pip")
                system("python get-pip.py")
            for i in list_of_model:
                system(f"pip install {i}")
            system(r"python.exe -m pip install --upgrade pip")
    else:
        print("Command '"+command[0]+"' is not any available command, programme or process.")
    print("Command finished")
