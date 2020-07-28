class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
             
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
    
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def __percolateDown(self):
        parentIndex = 0
        
        while True:
            childOIndex = 2*parentIndex + 1
            childtIndex = 2*parentIndex + 2
            
            if childOIndex >= self.getSize():
                break
            
            if childtIndex == self.getSize():
                if self.pq[childOIndex].ele > self.pq[parentIndex].ele:
                    self.pq[parentIndex], self.pq[childOIndex] = self.pq[childOIndex], self.pq[parentIndex]
                break
            
            # both child nodes exist    
            ele1 = self.pq[childOIndex].ele
            ele2 = self.pq[childtIndex].ele
            ele3 = self.pq[parentIndex].ele
            
            if (ele1 < ele3 and ele2 < ele3):
                break
            
            if (ele1 >= ele2) and (ele1 > ele3):
                self.pq[parentIndex], self.pq[childOIndex] = self.pq[childOIndex], self.pq[parentIndex]
                parentIndex = childOIndex
                continue
            
            if (ele2 >= ele1) and (ele2 > ele3):
                self.pq[parentIndex], self.pq[childtIndex] = self.pq[childtIndex], self.pq[parentIndex]
                parentIndex = childtIndex
                continue
            
    def removeMax(self):
        ans = self.pq[0].ele
        self.pq[0] = self.pq.pop()
        self.__percolateDown()
        return ans
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    