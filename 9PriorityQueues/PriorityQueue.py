class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        node = PriorityQueueNode(value, priority)
        self.pq.append(node)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        while parentIndex < self.getSize():
            child1Index = 2*parentIndex+1
            child2Index = 2*parentIndex+2 
            if child1Index < self.getSize() and (self.pq[child1Index].priority <= self.pq[child2Index].priority) and (self.pq[child1Index].priority < self.pq[parentIndex].priority):
                self.pq[child1Index], self.pq[parentIndex] = self.pq[parentIndex], self.pq[child1Index]
                parentIndex = child1Index
            elif child2Index < self.getSize() and (self.pq[child2Index].priority < self.pq[child1Index].priority) and (self.pq[child2Index].priority < self.pq[parentIndex].priority):
                self.pq[child2Index], self.pq[parentIndex] = self.pq[parentIndex], self.pq[child2Index]
                parentIndex = child2Index
            else:
                break

    def removeMin(self):
        if self.isEmpty():
            return None

        ele = self.pq[0].value
        self.pq[0], self.pq[self.getSize()-1] = self.pq[self.getSize() -
                                                        1], self.pq[0]
        self.pq.pop()
        print(self.pq)
        self.__percolateDown()
        return ele

pq = PriorityQueue()

pq.insert("A", 10)
pq.insert("C", 5)
pq.insert("B", 19)
pq.insert("D", 4)

for i in range(4):
    print(pq.removeMin())