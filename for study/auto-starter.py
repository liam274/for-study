def main():
    import subprocess
    import os
    no=("no","n","","nope","no way")
    if input("Do you want to start the study helper?") not in no:
        subprocess.Popen([r"C:\Users\Liam\AppData\Local\Programs\Python\Python312\python.exe","main.py"])
        os.system("cls")
main()
