class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    class LinkedList:
        def __init__(self):
            self.head=None
        def begin(self,data):
            new=Node(data)
            if self.head is None:
                self.head=new
                return None
            else:
                new.next=self.head
                self.head=new
        def insert(self,data,index):
            new=Node(data)
            cur=self.head
            pos=0
            if pos==index:
                self.begin(data)
            else:
                while cur!=None and pos+1!=index:
                    pos+=1
                    cur=cur.next
                if cur is not None:
                    new.next=cur.next
                    cur.next=new
                else:
                    raise IndexError("Index not present")
        def end(self,data):
            new=Node(data)
            if self.head is None:
                self.head=new
                return None
            cur=self.head
            while cur.next:
                cur=cur.next
        def update(self,val,index):
            cur=self.head
            pos=0
            if pos==index:
                cur.data=val
            else:
                while cur is not None and pos!=index:
                    pos+=1
                    cur=cur.next
                if cur is not None:
                    cur.data=val
                else:
                    raise IndexError("Index not present")
        def refirst(self):
            if self.head is None:
                return None
            self.head=self.head.next
        def relast(self):
            if self.head is None:
                return None
            while cur.next.next:
                cur=cur.next
            cur.next=None
        def remove(self,index):
            if self.head is None:
                return None
            cur=self.head
            pos=0
            if pos==index:
                self.refirst()
            else:
                while cur is not None and pos+1!=index:
                    pos+=1
                    cur=cur.next
                if cur is not None:
                    cur.next=cur.next.next
                else:
                    raise IndexError("Index not present")
        def removeN(self,data):
            cur=self.head
            while cur is not None and cur.next.data!=data:
                cur=cur.next
            if cur is None:
                return None
            else:
                cur.next=cur.next.next
        def size(self):
            size=0
            if self.head:
                cur=self.head
                while cur:
                    size+=1
                    cur=cur.next
                return size
            return 0
        def __repr__(self):
            cur=self.head
            _=[]
            while cur:
                _.append(cur.data)
                cur=cur.next
            return str(_)
        def __str__(self):
            cur=self.head
            _=[]
            while cur:
                _.append(cur.data)
                cur=cur.next
            return str(_)
        
