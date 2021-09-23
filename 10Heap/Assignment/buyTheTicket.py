# Buy the ticket
# Send Feedback
# You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.
# A queue is maintained for buying the tickets and every person has attached with a priority (an integer, 1 being the lowest priority). The tickets are sold in the following manner -
# 1. The first person (pi) in the queue asked to comes out.
# 2. If there is another person present in the queue who has higher priority than pi, then ask pi to move at end of the queue without giving him the ticket.
# 3. Otherwise, give him the ticket (and don't make him stand in queue again).
# Giving a ticket to a person takes exactly 1 minutes and it takes no time for removing and adding a person to the queue. And you can assume that no new person joins the queue.
# Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0). Find and return the time it will take until you get the ticket.
# Input Format :
# Line 1 : Integer N (Total number of people standing in queue)
# Line 2 : Priorities of every person (n space separated integers)
# Line 3 : Integer k (index of your priority)
# Output Format :
# Time required
# Sample Input 1 :
# 3
# 3 9 4
# 2

def timeTaken(lst, k):
    
    time_count = 0
    
    while True:
        if k == -1:
            return time_count
        
        coming = lst[0]
        
        if coming != max(lst):
            lst = lst[1:]
            lst.append(coming)
            k -= 1
            
            if k < 0:
                k = len(lst) -1
                
            continue
        
        lst = lst[1:]
        k -= 1
        time_count += 1
        

n = int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=timeTaken(lst, k)
print(ans)