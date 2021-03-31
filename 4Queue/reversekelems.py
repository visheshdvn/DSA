import queue

def reverseFirstK(q, k):
    if k == 0:
        return q

    element = q.get()

    q1 = reverseFirstK(q, k-1)

    q1.put(element)

    return q1


from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())

q1 = reverseFirstK(q, k)

if k < n:
    nums = n - k
    while nums:
        data = q1.get()
        q1.put(data)
        nums -= 1

while(q1.qsize()>0):
	print(q1.get())
	n-=1