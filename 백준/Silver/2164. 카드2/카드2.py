import sys
from collections import deque

num = int(input())

lists = deque([i for i in range(1,num+1)])

cnt = 0
while len(lists) >= 2:
    if cnt % 2 == 0:
        lists.popleft()
    else :
        a = lists.popleft()
        
        lists.append(a)
        
    cnt +=1

print(lists[0])
        
        