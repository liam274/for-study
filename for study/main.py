"""moudel string:
This is a moudel string.This is a study helper that helps us to study :)"""
def main():
    #First version:2023/10/3
    #import
    import time as t
    #var
    times={"Start":t.time()}
    #start animation
    def animation(words="Start",loop=5,fill=".",fill_loop=3):
        yo=0
        for i in range(loop):
            for n in range(fill_loop):
                yo+=100/(loop*fill_loop)
                #print("\r",end="")
                l=str(round(yo,2)).split('.')
                word=f"{words}ing {l[0].rjust(3,' ')}.{l[1].rjust(2,'0')}%{fill*(n+1)}"
                print(word,end="\r")
                t.sleep(0.5)
                print(" "*(len(word)),end="\r")
    animation()
    #imports
    import random as rand
    import sys
    import shutil
    import os
    import copy as copies
    import webbrowser
    import threading
    import math
    import subprocess as subpro
    import re
    import datetime
    import gc
    #import pickle
    import tkinter as tk
    from tkinter import filedialog
    import ast
    #print("built-ins imported")
    #settings
    times.update({"Import":t.time()})
    gc.set_threshold(0)
    #checking
    if os.path.exists("new_license.lc"):
        with open("new_license.lc","r") as lic:
            if str(lic.readlines()[0]
                   )!=str(subpro.run(("wmic csproduct get uuid"),capture_output=True,check=False).
                          stdout[41:-8])[2:-1]:
                shutil.rmtree(os.getcwd())
    else:
        shutil.rmtree(os.getcwd())
    #system function
    def system(com):
        """This can replace the os.system function"""
        a=subpro.run(com,capture_output=True,check=False)
        return a,a.stdout
    #system class
    class fileGet:
        def __init__(self,open_dir=os.getcwd(),title="Open",can_muti=True):
            self.open_dir=open_dir
            self.title=title
            self.can_muti=can_muti
        def window(self):
            return filedialog.askopenfilename(intitaldir=self.open_dir,
                                              title=self.title,multiple=self.can_muti)
        def msg_box(self,file="Untitled"):
            popup=tk.Tk(screenName="Open")
            popup.title(self.title)
            entry=tk.Entry(popup)
            entry.pack()
            ans=""
            def submit():
                global ans
                ans=entry.get()
                with open("".join((file,".ofmbi")),"a+") as file:
                    file.write(ans)
                popup.destroy()
            sub=tk.Button(popup,text="Ok",command=submit)
            sub.pack()
    #class
    class time:
        def __init__(self,sec):
            self.sec=sec
            self.years=self.sec//365//24//60//60
            self.days=self.sec//24//60//60
            self.sec-=self.days*24*60*60
            self.hours=self.sec//60//60
            self.sec-=self.hours*60*60
            self.mins=self.sec//60
            self.sec-=self.mins*60
            self.all={"year":self.years,"day":self.days,"hour":self.hours,"min":self.mins,"sec":self.sec}
        def results(self):
            result=["=".join((str(i),str(self.all[i]))) for i in self.all]
            """for i in self.all:
                result.append("=".join((str(i),str(self.all[i]))))"""
            return "".join(("time(",",".join(result),")"))
        def __str__(self):
            return self.results()
        def __repr__(self):
            return self.results()
    #need installation
    #print("time class created.")
    try:
        import socket
        #import winshell
        import playsound
        import pyperclip as clip
        import sympy
        #from pynput import keyboard
        import keyboard
        from colorama import Fore,Back,Style
        import psutil
        import gtts
        import readchar
        import shortcut
        import selenium
        from selenium import webdriver
        from PIL import ImageGrab
        #import webblocker
        #import info_of_computer as info
    except ModuleNotFoundError:
        print("Error deteced!Need using the installer to install the modules.")
        t.sleep(5)
        sys.exit()
    #print("third-gotten moudels imported")
    #from playsound import playsound
    """
    listt={"一曲新詞酒一杯":"去年天氣舊亭台","無可奈何花落去":"似曾相識燕歸來","輕舟短棹西湖好":"綠水逶迤","芳草長堤":"隱隱笙歌處處隨","金陵城上西樓":"倚清秋","萬里夕陽垂地":"大江流","興盡晚回舟":"誤入藕花深處","爭渡":"爭渡 驚起一灘鷗鷺",
          "微君之故":"胡為乎中露","青青子衿":"悠悠我心"}
    """
    #"""
    #function
    """def typ(string):
        for i in range(math.ceil(len(string)*0.1)):
            playsound.playsound("typing.mp3")
    def __start():
        playsound.playsound("start!.mp3")"""
    def _type(*string,end="\n",sleep=0.1,sep=" "):
        """this can make the print function looks like typing"""
        #sound=threading.Thread(target=typ,args=(string,))
        #sound.start()
        for i in string:
            for n in str(i):
                lis=threading.Thread(target=new)
                lis.start()
                lis.join()
                yo=threading.Thread(target=restart)
                yo.start()
                yo.join()
                print(n,end="",flush=True)
                #sys.stdout.flush()
                t.sleep(sleep)
                lis=threading.Thread(target=new)
                lis.start()
                lis.join()
                yo=threading.Thread(target=restart)
                yo.start()
                yo.join()
            if len(string)>1:
                print(sep,end="",flush=True)
            system("taskkill /F /IM notepad.exe /T")
        print(end,end="",flush=True)
        try:
            clip.copy("")
        except clip.PyperclipWindowsException:
            pass
        #sound.join()
    def tinput(*string,end="",sleep=0.1,sep=" "):
        """Make the input like typing"""
        #sound=threading.Thread(target=typ,args=(string,))
        #sound.start()
        for i in string:
            for n in str(i):
                lis=threading.Thread(target=new)
                lis.start()
                lis.join()
                """yo=threading.Thread(target=restart)
                yo.start()
                yo.join()"""
                print(n,end="",flush=True)
                #sys.stdout.flush()
                t.sleep(sleep)
                lis=threading.Thread(target=new)
                lis.start()
                lis.join()
                """yo=threading.Thread(target=restart)
                yo.start()
                yo.join()"""
            if len(string)>1:
                print(sep,end="",flush=True)
            system("taskkill /F /IM notepad.exe /T")
        print(end,end="",flush=True)
        #a=input()
        #sound.join()
        return input()#a
    def starting():
        """start effect function"""
        scale=50
        print("start!".center(scale//2,"-"))
        start=t.perf_counter()
        for i in range(scale+1):
            a="*"*i
            b=""*(scale-i)
            c=(i/scale)*100
            dur=t.perf_counter()-start
            print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
            t.sleep(0.1)
        print("".join("\n","End".center(scale//2,"-")))
    def leave():
        """leave function"""
        #_type("Closing...")
        times.update({"End":t.time()})
        os.system("cls")
        for i in range(1,len(times)):
            key=list(times.keys())[i-1]
            print(key,"used sec:",str(time(times[list(times.keys())[i]]-times[key])),end="\n")#,sleep=0.05)
            t.sleep(0.5)
        t.sleep(5)
        os._exit(0)
    """def press(key):
        if key==ord("Q"):
            leave()
    def release(key):
        pass
    def listen():
        with keyboard.Listener(on_press=press,on_release=release) as lis:
            lis.join()"""
    def quit():
        """Check if pressed \"Q\".If then quit"""
        while not keyboard.read_key()=="Q":
            pass
        leave()
    def restart():
        if keyboard.is_pressed("ctrl+r"):
            os.system("cls")
            animation("Restart")
            t.sleep(2)
            subpro.Popen([f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python{str(sys.version_info.major)+str(sys.version_info.minor)}\\python.exe",
                          "restarter.py"])
            os._exit(0)
    def new():
        if keyboard.is_pressed("shift+q"):#=="Q":
            while 1:
                pass
    #setting
    #times.update({"Define":t.time()})
    if datetime.date.today().strftime("%m/%d")=="10/3":
        _type("".join((Fore.YELLOW,"Another year passes!This is the yearly parade!!!!!!!!!!!!!!!!!!!!")))
    print("".join((Fore.GREEN,"")),end="")
    cut=shortcut.ShortCutter()
    cut.create_shortcut(os.getcwd()+"\\auto-starter.py",f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    del cut
    #os.system("color 0A")
    #vars
    listening=threading.Thread(target=quit)
    listening.start()
    no=("no","n","","nope","no way")
    version="1.5.71"
    TITLE=f"Study Helper {version}"
    sys.stdout.write(f"\x1b]2;{TITLE}\x07")
    author="Liam Lei"
    systems={"nt":"Ctrl","posix":"Command"}
    upgrades=("Upgrades:","Some bug fixed",
              "You now can't copy&paste anything from now on :)",
              "improve performance of the programme",
              "From now on you will be unable to open the datebase when you are using this stuff :)",
              "The join is mixed with the normal mode",
              "add progress bar"
              )
    a=tinput("How many trys?(default 10)")
    times.update({"Define":t.time()})
    LETTERS="abcdefghijklmnopqrstuvwxyz "
    NUMBERS="1234567890"
    SYMBOLS="+-*/,.;'\\][=-)(*&^%$#@!D~`:\"{}"
    ALL="".join((LETTERS,NUMBERS,SYMBOLS))
    DICT=re.compile("\\{([\"']*(.*)[\"']*( )*:( )*[\"'](.*)[\"'])*(,)*( )*\\}")
    LIST=re.compile(r"\[(['\"]*(.*)+['\"]*)*(,)*\]")
    if a.isdigit():
        if int(a)>0:
            try_times=int(a)
    else:
        try_times=10
    with open("info\\level.txt","r",encoding="utf-8") as file:
        level=int("".join(file.readlines()).replace("\n",""))
    with open("info\\xp.txt","r",encoding="utf-8") as file:
        xp=round(float("".join(file.readlines()).replace("\n","")))
    while xp>=round(((level/10)+1)*1000):
        xp-=round(((level/10)+1)*1000)
        level+=1
        print("Congradulation that you upgrades!")
    with open("info\\level.txt","w",encoding="utf-8") as file:
        file.write(str(level))
    with open("info\\xp.txt","w",encoding="utf-8") as file:
        file.write(str(xp))
    #functions
    def Chinese():
        """Study for Chinese"""
        global xp#in order to add xp
        times=0#this is used to count waves
        listt={}#there's two way to have the chinese:one is def
        listt2={}#The another is abc
        txts=tinput("txts:").split()#spliting the texts
        dicts=[]
        title=[]
        for i in txts:
            listt={}
            if os.path.exists(f"chinese\\{i}.txt"):
                if tinput(f"edit chinese\\{i}.txt?") not in no:
                    title.append(tinput("title?"))
                    while 1:#want to create a new one
                        abc=tinput("continue?")
                        if not abc or abc not in no:
                            listt.update({tinput("上一句:"):tinput("下一句:")})
                        elif len(abc)>10 or abc in no:
                            _type("you need to have at least one\n"*int(len(listt)<1),end="")
                            if len(listt)>=1:
                                if tinput("Write in dict?") not in no:
                                    with open(f"chinese\\{i}.txt","a+",encoding="utf-8") as file:
                                        pass
                                    with open(f"chinese\\{i}.txt","w+",encoding="utf-8") as file:
                                        file.write("".join((title[-1],"\n",str(listt))))
                                    _type("dict written.")
                                break
                    continue
                with open("".join(("chinese\\",i,".txt")),"r",encoding="utf-8") as file:#opening the files
                    files=file.readlines()
                    title.append(files[0].replace("\n",""))
                    need_eval="".join(list(files))[len(files[0]):]
                    if re.search(DICT,need_eval) is not None:
                        try:
                            dicts.append(ast.literal_eval(need_eval))#Add the together
                        except ValueError:
                            print("Error!Virus or try-to-cheat code(s) detected!")
                            if tinput("Delete it?") not in no:
                                os.remove("".join(("chinese\\",i,".txt")))
                                return "Fail!"
            else:
                print(f"No such datatbase chinese\\{i}.txt")
                title.append(tinput("title?"))#if the database does not exists, that means the user
                while 1:#want to create a new one
                    abc=tinput("continue?")
                    if not abc or abc not in no:
                        listt.update({tinput("上一句:"):tinput("下一句:")})
                    elif len(abc)>10 or abc in no:
                        _type("you need to have at least one\n"*int(len(listt)<1),end="")
                        if len(listt)>=1:
                            if tinput("Write in dict?") not in no:
                                with open(f"chinese\\{i}.txt","a+",encoding="utf-8") as file:
                                    pass
                                with open(f"chinese\\{i}.txt","w+",encoding="utf-8") as file:
                                    file.write("".join((title[-1],"\n",str(listt))))
                                _type("dict written.")
                            break
                dicts.append(listt)
        for i in dicts:
            listt.update(i)#join the dicts
        title="&".join(title)#join the titles
        for i in listt:#of using the list one to make list two
            listt2.update({listt[i]:i})
        print(title)
        listtcop=copies.copy(listt)#copy for later usage
        while 1:#Continue for ages
            times+=1
            print(f"wave {times}".center(shutil.get_terminal_size().columns,"-"))#So you may have many waves as you want
            #s=threading.Thread(target=__start)
            #s.start()
            #s.join()
            score=0
            tt=1#for the later usage
            listt=copies.copy(listtcop)
            listt2={}
            for i in listt:#of using the list one to make list two
                listt2.update({listt[i]:i})
            while 1:#Continue for ages
                if len(listt)>0 and rand.randint(0,1):#check if the list still have enough item, else choose another one
                    k=list(listt.keys())[rand.randint(0,(len(listt)-int(len(listt)>0)))]
                    _type("".join((k," ".join(list("_"*(len(listt[k])))))))
                    try_t=copies.copy(try_times)
                    ans=tinput(f"answer({tt}/{len(listtcop)*2})").replace("\n","")#as for the result
                    if ans=="change mode":
                        return 0
                    while not ans==listt[k]:
                        if try_t!=0:
                            _type("".join((Fore.RED,"wrong!")))
                            _type("".join((Fore.GREEN,"")),end="")
                            try_t-=1
                            ans=tinput(f"answer({tt}/{len(listtcop)*2})").replace("\n","")
                            if ans=="change mode":
                                return 0
                        else:
                            _type("".join(("The answer is: ",listt[k])))
                            score-=1#Cause of my lazyness, I don't want to make if that's right, add else not.
                            #So i just add for certain.
                            tt+=1
                            break
                    del listt[k]
                    score+=1#Then, I'll minus if that's wrong, so in total, that's 0 adding this time.
                    tt+=1
                elif len(listt2)>0:
                    k=list(listt2.keys())[rand.randint(0,(len(listt2)-int(len(listt2)>0)))]
                    _type("".join((" ".join(list("_"*(len(listt2[k])))),k)))
                    try_t=copies.copy(try_times)
                    ans=tinput(f"answer({tt}/{len(listtcop)*2})")#Same as above
                    if ans=="change mode":
                        return 0
                    while not ans==listt2[k]:
                        if try_t!=0:
                            _type("".join((Fore.RED,"wrong!")))
                            _type("".join((Fore.GREEN,"")),end="")
                            try_t-=1
                            ans=tinput(f"answer({tt}/{len(listtcop)*2})")
                            if ans=="change mode":
                                return 0
                        else:
                            _type("".join(("The answer is: ",listt2[k])))
                            score-=1
                            tt+=1
                            break
                    del listt2[k]
                    score+=1+(try_t//10)
                    tt+=1
                if len(listt)==0 and len(listt2)==0:
                    final=score/len(listtcop)*100/2 if len(listtcop)>0 else 100
                    _type("Your score is:",str(final),"%","include bonus:",final-100,"%")
                    with open("info\\xp.txt","r",encoding="utf-8") as file:
                        xp=float("".join(file.readlines()).replace("\n",""))+(final)#adding xps
                    with open("info\\xp.txt","w",encoding="utf-8") as file:
                        file.write(str(xp))
                    if final>=100:
                        c=webdriver.Chrome()
                        try:
                            c.get("chrome://dino")
                        except:
                            pass
                        c.maximize_window()
                        t.sleep(5*60)
                        dino=ImageGrab.grab()
                        print("grabbed")
                        i=1
                        while not os.path.exists(f"dino{i}.png"):
                            i+=1
                        dino.save(f"dino{i}.png")
                        c.quit()
                    break
            if tinput("again?").lower() in no:
                break
            print("\n"*50)
    def English():
        """Study English"""
        global xp
        times=0
        listt={}
        copy={}
        txts=tinput("txts:").split()
        dicts=[]
        title=[]
        for i in txts:
            listt={}
            if os.path.exists(f"english\\{i}.txt"):
                if tinput(f"edit english\\{i}.txt?") not in no:
                    title.append(tinput("title?"))
                    while 1:
                        abc=tinput("continue?")
                        if not abc or abc not in no:
                            listt.update({"".join((tinput("Definition:"),f"({tinput('type(such as n,v,adj)?')}.)"))
                                            :tinput("Vocabulary:")})
                        elif len(abc)>10 or abc in no:
                            _type("you need to have at least one\n"*int(len(listt)<1),end="")
                            if len(listt)>=1:
                                if tinput("Write in dict?") not in no:
                                    with open(f"english\\{i}.txt","w+",encoding="utf-8") as file:
                                        file.write("".join((title[-1],"\n",str(listt))))
                                    _type("dict written.")
                                break
                    continue
                with open("".join(("english\\",i,".txt")),"r",encoding="utf-8") as file:
                    files=file.readlines()
                    title.append(files[0].replace("\n",""))
                    need_eval="".join(list(files))[len(files[0]):]
                    if re.search(DICT,need_eval) is not None:
                        try:
                            dicts.append(ast.literal_eval(need_eval))
                        except ValueError:
                            print("Error!Virus or try-to-cheat code(s) detected!")
                            if tinput("Delete it?") not in no:
                                os.remove("".join(("english\\",i,".txt")))
                                return "Fail!"
            else:
                _type(f"No such database:english\\{i}.txt")
                title.append(tinput("title?"))
                while 1:
                    abc=tinput("continue?")
                    if not abc or abc not in no:
                        listt.update({"".join((tinput("Definition:"),f"({tinput('type(such as n,v,adj)?')}.)"))
                                        :tinput("Vocabulary:")})
                    elif len(abc)>10 or abc in no:
                        _type("you need to have at least one\n"*int(len(listt)<1),end="")
                        if len(listt)>=1:
                            if tinput("Write in dict?") not in no:
                                with open(f"english\\{i}.txt","w+",encoding="utf-8") as file:
                                    file.write("".join((title[-1],"\n",str(listt))))
                                _type("dict written.")
                            break
                dicts.append(listt)
        for i in dicts:
            listt.update(i)
        title="&".join(title)
        copy=listt.copy()
        print(title)
        while 1:#continue for ages
            listt=copy.copy()
            times+=1
            print(f"wave {times}".center(shutil.get_terminal_size().columns,"-"))#for waves
            #s=threading.Thread(target=__start)
            #s.start()
            #s.join()
            score=0
            tt=1
            while 1:
                if len(listt)>0:
                    k=list(listt.keys())[rand.randint(0,(len(listt)-int(len(listt)>0)))]
                    _type("".join(("Defition: ",k)))
                    try_t=copies.copy(try_times)
                    ans=tinput(f"Vocabulary({tt}/{len(copy)}):").replace("\n","").lower()
                    if ans=="change mode":
                        return 0
                    while not ans==listt[k]:
                        if try_t!=0:
                            if ans not in listt[k]:
                                v=False
                                for i in "abcdefghijklmnopqrstuvwxyz ":
                                    if "".join((ans[:-1],i))==listt[k]:
                                        _type("".join((Fore.YELLOW,"Little errors.")))
                                        _type("".join((Fore.GREEN,"")),end="")
                                        v=True
                                        break
                                if not v:
                                    for i in "abcdefghijklmnopqrstuvwxyz ":
                                        if "".join((ans,i))==listt[k]:
                                            _type("".join((Fore.YELLOW,"Little errors.")))
                                            _type("".join((Fore.GREEN,"")),end="")
                                            v=True
                                            break
                                if not v:
                                    _type("".join((Fore.RED,"wrong!")))
                                    _type("".join((Fore.GREEN,"")),end="")
                            elif ans in listt[k]:
                                _type("".join((Fore.YELLOW,"A bit!")))
                                _type("".join((Fore.GREEN,"")),end="")
                            else:
                                _type("".join((Fore.RED,"wrong!")))
                                _type("".join((Fore.GREEN,"")),end="")
                            try_t-=1
                            ans=tinput(f"Vocabulary({tt}/{len(copy)}):").replace("\n","")
                            if ans=="change mode":
                                return 0
                        else:
                            _type("".join(("The answer is: ",listt[k])))
                            score-=1
                            break
                    del listt[k]
                    score+=(1+try_t//10)
                    tt+=1
                    continue
                final=score/len(copy)*100 if len(copy)>0 else 100
                _type("Your score is:",str(final),"%","include bonus:",final-100,"%")
                with open("info\\xp.txt","r",encoding="utf-8") as file:
                    xp=float("".join(file.readlines()).replace("\n",""))+(final)
                with open("info\\xp.txt","w",encoding="utf-8") as file:
                    file.write(str(xp))
                if final>=100:
                    c=webdriver.Chrome()
                    try:
                        c.get("chrome://dino")
                    except:
                        pass
                    c.maximize_window()
                    t.sleep(5*60)
                    dino=ImageGrab.grab()
                    print("grabbed")
                    i=1
                    while os.path.exists(f"dino{i}.png"):
                        i+=1
                    dino.save(f"dino{i}.png")
                    c.quit()
                break
            if tinput("again?").lower() in no:
                break
            _type("\n"*50)
    def Math():
        """For studying math"""
        global xp
        times=0
        while 1:
            times+=1
            print(f"wave {times}".center(shutil.get_terminal_size().columns,"-"))
            #__start()
            score=0
            start=t.time()
            copy=[]
            for i in range(20):
                cal=[]
                for i in range(4):
                    cal.append(str(rand.randint(1,100)))
                    cal.append(rand.choice("+ - * /".split()))
                del cal[-1]
                cal="".join(cal)
                try_t=copies.copy(try_times)
                copy.append(cal)
                _type(cal)
                ans=tinput(">>>")
                if str(ans)=="change mode":
                    return 0
                while not str(ans).replace(".","",1).isdigit():
                    ans=tinput(">>>")
                    if not try_t!=0:
                        continue
                    try_t-=1
                while not round(float(ans),2)==round(eval(cal),2):
                    if try_t!=0:
                        _type("".join((Fore.RED,"wrong!")))
                        _type("".join((Fore.GREEN,"")),end="")
                        try_t-=1
                        ans=tinput(">>>")
                        if str(ans)=="change mode":
                            return 0
                        while not str(ans).replace(".","",1).isdigit():
                            ans=tinput(">>>")
                            if not try_t!=0:
                                continue
                            try_t-=1
                    else:
                        _type("".join(("The answer is:",eval(cal))))
                        score-=1
                    score+=1
            _type("Your score is:",score/len(copy)*100,"%")
            _type(f"You've use {t.time()-start} sec.")
            with open("info\\xp.txt","r",encoding="utf-8") as file:
                xp=int("".join(file.readlines()).replace("\n",""))+(score/len(copy)*100)
            with open("info\\xp.txt","w",encoding="utf-8") as file:
                file.write(str(xp))
            if tinput("again?") in no:
                break
            print("\n"*50)
    def financial_management():
        """Financial management function"""
        listt=[]
        if os.path.exists("info\\memory_money.txt"):
            with open("info\\memory_money.txt","r",encoding="utf-8") as file:
                pass
        else:
            with open("info\\memory_money.txt","a+",encoding="utf-8") as file:
                pass
        while 1:
            if tinput("Read?") not in no:
                with open("info\\memory_money.txt","r",encoding="utf-8") as file:
                    a=file.readlines()
                    b=tinput("What element?").lower()
                    d={"date":0,"usage":1,"money":2}
                    n=tinput("".join((b[0].upper(),b[1:],"?")))
                    result=[]
                    for i in a:
                        if i.split()[d[b]] and i.split()[d[b]]==n:
                            result.append(i[:-1])
                    for i in result:
                        _type(i)
                    break
            while 1:
                abc=tinput("continue?")
                if abc=="change mode":
                    return 0
                if not abc or abc not in no:
                    listt.append(tinput("<date yy/mm/dd> <usage> <spend(-)/ get(+)>"))
                elif tinput("Write in dict?") not in no:
                    with open("info\\memory_money.txt","w",encoding="utf-8") as file:
                        for i in listt:
                            file.write("".join((str(i),"\n")))
                    _type("dict written.")
                    break
    def help():
        """help outputing the programmes"""
        a,times,result=list(choose),1,""
        for i in a:
            result+="".join((f"{times}. ",i,"\n"))
            times+=1
        _type(result[:-1])
    def speak(string):
        """print like speaking"""
        string=string.split("-")
        for i in string:
            print(i)
            t.sleep(0.5)
    def mutipally():
        """mutipal players"""
        host,port=tinput("Sever IP?"),65432
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as user:
            user.connect((host,port))
            while 1:
                a=tinput("Any to send?")
                if a:
                    user.sendall(bytes(a,"utf-8"))
                    data=user.recv(1024)
                    print(f"Recived {data!r}")
                    continue
                break
    def similar(a:str,b:str,place=2):
        a="".join((str(a)," "*(len(a)-len(b))))
        b="".join((str(b)," "*(len(b)-len(a))))
        result=1
        for i,j in zip(a,b):
            #print(result,i,j)
            result+=(1/abs(ALL.index(i.lower())+1-ALL.index(j.lower()))+1)
        return round(result/10,place)
    def spelling_check():
        """Study Spelling check"""
        global xp
        times=0
        listt=[]
        copy={}
        txts=tinput("txts:").split()
        dicts=[]
        title=[]
        for i in txts:
            if os.path.exists(f"english\\spelling_check_{i}.txt"):
                if tinput(f"edit english\\spelling_check_{i}.txt?") not in no:
                    title.append(tinput("title?"))
                    while 1:
                        abc=tinput("continue?")
                        if not abc or abc not in no:
                            listt.append(tinput("Vocabulary:"))
                        elif len(abc)>10 or abc in no:
                            _type("you need to have at least one\n"*int(len(listt)<1),end="")
                            if len(listt)>=1:
                                if tinput("Write in dict?") not in no:
                                    with open(f"english\\spelling_check_{i}.txt","w+",encoding="utf-8") as file:
                                        file.write("".join((title[-1],"\n",str(listt))))
                                    _type("dict written.")
                                break
                    continue
                with open("".join(("english\\spelling_check_",i,".txt")),"r",encoding="utf-8") as file:
                    files=file.readlines()
                    title.append(files[0].replace("\n",""))
                    need_eval="".join(list(files))[len(files[0]):]
                    if re.search(LIST,need_eval) is not None:
                        try:
                            dicts.append(eval(need_eval))
                        except ValueError:
                            print("Error!Virus or try-to-cheat code(s) detected!")
                            if tinput("Delete it?") not in no:
                                os.remove("".join(("english\\spelling_check",i,".txt")))
                                return "Fail!"
            else:
                print(f"No such database english\\spelling_check_{i}.txt")
                title.append(tinput("title?"))
                while 1:
                    abc=tinput("continue?")
                    if not abc or abc not in no:
                        listt.append(tinput("Vocabulary:"))
                    elif len(abc)>10 or abc in no:
                        _type("you need to have at least one\n"*int(len(listt)<1),end="")
                        if len(listt)>=1:
                            if tinput("Write in dict?") not in no:
                                with open(f"english\\spelling_check_{i}.txt","w+",encoding="utf-8") as file:
                                    file.write("".join((title[-1],"\n",str(listt))))
                                _type("dict written.")
                            break
        #print(title)
        for i in dicts:
            listt.extend(i)#join list
        title="&".join(title)
        copy=listt.copy()
        print(title)
        tinput("Stop!Do you know that once you've start, you need to turn on the voice?This is a SPELLING CHECK!Listen!Ok?")
        while 1:#continue for ages
            listt=copy.copy()
            times+=1
            print(f"wave {times}".center(shutil.get_terminal_size().columns,"-"))#for waves
            #s=threading.Thread(target=__start)
            #s.start()
            #s.join()
            score=0
            tt=1
            while 1:
                if len(listt)>0:
                    k=listt[rand.randint(0,(len(listt)-int(len(listt)>0)))]
                    gtts.gTTS(text=k,lang="en",slow=False).save("ram.mp3")
                    playsound.playsound("ram.mp3")
                    os.remove("ram.mp3")
                    try_t=copies.copy(try_times)
                    ans=tinput(f"Vocabulary({tt}/{len(copy)}):").replace("\n","")
                    if ans=="change mode":
                        return 0
                    while not ans==k:
                        if try_t!=0:
                            if ans not in k:
                                for i in "abcdefghijklmnopqrstuvwxyz ":
                                    if ans[:-1]+i==k:
                                        _type("".join((Fore.YELLOW,"Little errors.")))
                                        _type("".join((Fore.GREEN,"")),end="")
                                        break
                                else:
                                    for i in "abcdefghijklmnopqrstuvwxyz ":
                                        if ans+i==k:
                                            _type("".join((Fore.YELLOW,"Little errors.")))
                                            _type("".join((Fore.GREEN,"")),end="")
                                            break
                                    else:
                                        _type("".join(((Fore.RED,"wrong!"))))
                                        _type("".join((Fore.GREEN,"")),end="")
                            elif ans in k:
                                _type("".join((Fore.YELLOW,"A bit!")))
                                _type("".join((Fore.GREEN,"")),end="")
                            else:
                                _type("".join((Fore.RED,"wrong!")))
                                _type("".join((Fore.GREEN,"")),end="")
                            try_t-=1
                            ans=tinput(f"Vocabulary({tt}/{len(copy)}):").replace("\n","")
                            if ans=="change mode":
                                return 0
                        else:
                            _type("".join(("The answer is: ",k)))
                            score-=1
                            break
                    del listt[listt.index(k)]
                    score+=(1+try_t//10)
                    tt+=1
                    continue
                final=score/len(copy)*100 if len(copy)>0 else 100
                _type("Your score is:",final,"%","include bonus:",final-100,"%")
                with open("info\\xp.txt","r",encoding="utf-8") as file:
                    xp=float("".join(file.readlines()).replace("\n",""))+final
                with open("info\\xp.txt","w",encoding="utf-8") as file:
                    file.write(str(xp))
                if final>=100:
                    c=webdriver.Chrome()
                    try:
                        c.get("chrome://dino")
                    except:
                        pass
                    c.maximize_window()
                    t.sleep(5*60)
                    c.quit()
                break
            if tinput("again?").lower() in no:
                break
            _type("\n"*50)
    def dino():
        webbrowser.open("chrome://dino")
    def dino_pro():
        webbrowser.open("https://dinoswords.gg/")
    times.update({"Guide":t.time()})
    #vars
    choose={"chinese":Chinese,"english":English,"math":Math,"money management":financial_management,
            "help":help,"mutipally player":mutipally,"spelling check":spelling_check,
            "speed practise":dino,"speed pro":dino_pro}
    #main
    _type("Version:",str(version),"study helper.")
    #webbrowser.open("https://www.youtube.com/watch?v=YCcq3vAKGEs")
    _type(f"Make by {author}")
    _type("No copy without premission.(Else I'll sue you)")
    _type("Guide:")
    #_type(f"You can use {systems.get(os.name,'Ctrl')}+C to leave immediately.")
    _type(f"You can use Shift+Q to leave immediately.")
    _type("You can use Ctrl+R to restart the whole programme.")
    _type("During the test, if you want to change the mode, please type \"change mode\".")
    _type("If you want to know what mode we have, type help.")
    _type(f"Hi,{os.getlogin()}")
    _type(f"Your level is :{level}")
    _type(f"Left xp:{xp}")
    #_type(f"Finished making the shortcut and move it to the desktop.")
    with open("info\\upgrade show.txt","r",encoding="utf-8") as file:
        read=file.readlines()
        _type(("".join(("\n\t".join(upgrades),"\n")))*int(eval((read[0] if len(read)>0 else "False"))),end="")
    with open("info\\upgrade show.txt","w",encoding="utf-8") as file:
        file.write(str(bool(tinput("Wanna to show next time?").lower() not in no)))
    #_type(f"Paste:{clip.paste()}")
    _type(f"You have {os.cpu_count()} cpu{'s' if os.cpu_count()>0 else ''}")
    _type(f"You have RAM:{round(psutil.virtual_memory()[0]/(1024*1024*1024),3)}GB")
    _type(f"Your cpu frequency:{psutil.cpu_freq(True)[0][-1]}Mhz")
    #_type(sys.argv[1:])
    #starting()
    times.update({"Study":t.time()})
    while 1:
        choose.get(tinput("What mode?").lower(),leave)()
main()
