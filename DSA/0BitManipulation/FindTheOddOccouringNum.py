from curses.ascii import NL


n = [int(i) for i in input().split()]

num = 0

for i in n:
    num = num^i

print(num)