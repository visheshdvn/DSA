import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q1size = 0
        self.q2size = 0
        self.first = None
        
        
    def push(self,data):
        self.first = data
        self.q1.put(data)
        self.q1size += 1

    def pop(self):
        while self.q1size != 1:
            self.q2.put(self.q1.get())
            self.q1size -= 1
            self.q2size += 1
            self.tp = 0

        data = self.q1.get()
        self.q1size -= 1

        while self.q2size:
            self.first = self.q2.get()
            self.q1.put(self.first)
            self.q2size -= 1
            self.q1size += 1

        return data

    def top(self):
        if self.q1size == 0:
            return -1
        
        return self.first
        
    def getSize(self):
        return self.q1size

    
s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')
            
    i+=1