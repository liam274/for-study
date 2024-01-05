import math
class binNotEnough(Exception):
    pass
class binTooBig(Exception):
    pass
class noSuchStyle(Exception):
    pass
def half_add(a,b):
    return not(a and b),a and b
def full_add(a,b,cin=0):
    return a^b^cin,(a&b)|(cin&(a^b))
def muti_add(a,b,cin=0):
    a,b=list(a)[::-1],list(b)[::-1]
    a+=[False]*(len(b)-len(a))
    b+=[False]*(len(a)-len(b))
    r=[]
    for i in range(len(a)):
        s,out=full_add(a[i],b[i],cin)
        r.append(s)
        cin=out
    if cin:
        r.append(cin)
    return tuple(r[::-1])
"""def muti_minus(a,b,cin=0):
    #b2=b
    #b=flip(b)
    r=muti_add(a,flip(b),cin)
    if int("".join(map(str,a)),2)<int("".join(map(str,b)),2):
        return ("a",)+flip(r[1:])#,r[1:]
    return r[1:]"""
def muti_minus(a,b):
    a=(0,)*(max((len(a),len(b)))-len(a))+a
    b=(0,)*(max((len(a),len(b)))-len(b))+b
    bb=0
    r=[]
    for i in range(max((len(a),len(b)))-1,-1,-1):
        if a[i]==0 and b[i]==0:
            if bb==0:
                r.insert(0,0)
            else:
                r.insert(0,1)
                bb=0
        elif a[i]==1 and b[i]==0:
            if bb==0:
                r.insert(0,1)
            else:
                r.insert(0,0)
                bb=1
        elif a[i]==0 and b[i]==1:
            if bb==0:
                r.insert(0,0)
                bb=1
            else:
                r.insert(0,1)
        elif a[i]==1 and b[i]==1:
            if bb==0:
                r.insert(0,1)
            else:
                r.insert(0,0)
                bb=1
    return (("a",) if int("".join(map(str,a)),2)<int("".join(map(str,b)),2) else ())+tuple(r)
def muti_muti(a,b):
    zs=[False]*(len(a)+len(b))
    for i in range(len(a)):
        if a[i]==True:
            c=0
            for j in range(len(b)):
                t=zs[i+j]+int(b[len(b)-1-j])+c
                zs[i+j]=t%2
                c=t//2
            zs[i+len(b)]=c
    return tuple(map(int,zs))
def muti_div(a,b):
    if len(b)>len(a):
        return 0,a
    q=(0,)
    remain=a
    while True:
        r=muti_minus(remain,b)
        print(r)
        if r[0]!="a":
            q=muti_add(q,(True,))
            remain=r
            print(remain,q)
        else:
            break
    return q,remain
    return tuple(map(int,tuple(q))),remain
def bool(input):
    return input in ("True",1)
def flip(b):
    return muti_add(tuple(map(lambda x:False if x else True,b)),(True,))
class _bin:
    def __init__(self,digit:int):
        self.bin=self.to_bin(digit)
        self.style="int"
        self._style()
        #return self.bin
    def to_bin(self,digit:int):
        a=[]
        for i in str(bin(digit))[2:]:
            a.append(i=="1")
        return tuple(a)
    def int(self):
        return int("".join(map(str,self.bin)),2)
    def add(self,other):
        self.bin=muti_add(self.bin,other.bin)
        return self.bin
    def flip(self):
        self.bin=muti_add(tuple(map(lambda x:not x,self.bin)),(True,))
        self._style()
        return self.bin
    def _style(self,style="int"):
        self.style=style
        if self.style=="int":
            self.bin=tuple(map(int,self.bin))
        elif self.style=="bool":
            self.bin=tuple(map(bool,self.bin))
        elif self.style=="str int":
            self.bin=tuple(map(str,map(int,self.bin)))
        elif self.style=="str bool":
            self.bin=tuple(map(str,map(bool,self.bin)))
        else:
            raise noSuchStyle("No such style:{self.style}")
        return self.bin
    def minus(self,other):
        self.bin=self.__sub__(other)
        return self.bin
    def muti(self,other):
        self.bin=self.__mul__(other)
        return self.bin
    #   beautiful
    #conut
    def __add__(self,other):
        return muti_add(self.bin,other.bin)
    def __sub__(self,other):
        return muti_minus(self.bin,other.bin)
    def __mul__(self,other):
        return muti_muti(self.bin,other.bin)
    def __truediv__(self,other):
        return muti_div(self.bin,other.bin)
    #show
    def __repr__(self):
        return f"{''.join(map(str,self.bin))} in bin or {self.int()} in dec."
    def __str__(self):
        return self.__repr__()
