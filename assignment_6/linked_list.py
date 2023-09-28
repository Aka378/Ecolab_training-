
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,data):
        newN = Node(data)
        if self.head==None:
            self.tail = newN
            self.head = newN
        else:
            self.tail.next = newN
            self.tail = newN
        self.size+=1

    def insert(self,pos,data):
        if pos<0 and pos>self.size:
            print("Invalid position")
        
        newN = Node(data)
        if pos==0:
             newN.next = self.head
             self.head = newN
             return
        
        cur = self.head
        prev = None
        count = 0
        while count<pos and cur:
            prev = cur
            cur = cur.next
            count+=1
        if count==pos:
            prev.next=newN
            newN.next=cur
        else:
            print('Position out of range')
        
        self.size +=1

    def remove(self,pos):
        if pos<0 or pos>=self.size:
            print("Invalid position")
            return None
        
        if pos==0:
             rem_data = self.head.data
             self.head = self.head.next
             self.size-=1
             return rem_data
        
        cur = self.head
        prev = None
        count = 0

        while count<pos and cur:
            prev = cur
            cur = cur.next
            count+=1

        if count==pos:
            rem_data = cur.data
            prev.next = cur.next

            if count == self.size-1:
                self.tail = prev
            self.size-=1
            return rem_data
            
        else:
            print('Position out of range')
            return None
        
        

    def get(self,pos):
        cur = self.head
        for i in range(pos-1):
            cur = cur.next
        return cur.next.data
    
    def set(self,pos,data):
        cur = self.head
        for i in range(pos-1):
            cur = cur.next
        cur.data = data

    def sizeofL(self):
        return self.size
    
    def info(self):
        cur = self.head
        for i in range(self.size-1):
            print(f'{cur.data}->',end="")
            cur = cur.next
        print("None")

    def remove(self,pos):
        if pos<0 and pos>self.size:
            print("Invalid position")
                  
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
            

            
SLL=LinkedList()
for i in range(10):
    SLL.append(i+1)
SLL.insert(6,5)
SLL.info()
SLL.remove(0)

SLL.info()

 