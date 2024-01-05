import math
import random
def Max(lis):
    return lis[1]
def _max(score):
    """the score is a list"""
    if isinstance(score,list):
        nn=[]
        s=0
        for i in score:
            s+=i[2]*i[1]
            nn.append((i[0],i[2]*i[1]))
        m=max(nn,key=Max)
        return m[1],m,nn,s
class Genetic:
    def __init__(self,lis,function=_max):
        """lis       for the elements of the value(s)
The format is:
[(<value_name>,<weights>,<max_of_this_elements>,<min_of_this_element>)]
function       for giving the final score for the value(s)"""
        self.lis=lis
        self.func=function
        self.manys=[]
        self.max=0
        self.best=None
    def random(self):
        new=self.lis.copy()
        random.shuffle(new)
        n=[]
        for i in new:
            n.append((i[0],i[1],random.uniform(i[2],i[3]),i[2],i[3]))
        self.lis=n#[(<value_name>,<weights>,<value>,<max>,<min>)]
        ren=self.func(self.lis)
        if ren[3]>self.max:
            self.max=ren[3]
            self.best=ren[2]
        return ren[1]
    def random_many(self,times=100):
        for i in range(times if isinstance(times,int) else 100):
            self.random()
        return self.best
        
