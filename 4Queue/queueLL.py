
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class QueueUsingLL:
  
### Implement These Functions Here    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.count = 0
        
    def enqueue(self,data):
        node = Node(data)

        if self.__head == None:
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = self.__tail.next

        self.count += 1
        
    def dequeue(self):
        if self.__head == None:
            return -1

        node = self.__head
        self.__head = self.__head.next
        node.next = None
        n = node.data
        node = None
        self.count -= 1
        return n

    def front(self):
        return self.__head.data
        
    def isEmpty(self):
        return self.__head == None
    
    def getSize(self):
        return self.count


    
q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getSize())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1