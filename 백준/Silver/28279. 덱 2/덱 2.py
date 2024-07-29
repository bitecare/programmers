import sys
from collections import deque

lists = deque()

def one(x, list = lists):
    list.appendleft(x)
    
    return list

def two(x, list = lists):
    list.append(x)
    
    return list

def three(list = lists):
    if len(list) == 0:
        print(-1)
    else :
        b = list.popleft()
        print(b)
        
    return list

def four(list = lists):
    if len(list) == 0:
        print(-1)
    else :
        b = list.pop()
        print(b)
        
    return list

def five(list = lists):
    print(len(list))
    
    return list

def six(list = lists):
    if len(list) == 0 :
        print(1)
    else :
        print(0)
        
    return list

def seven(list = lists):
    if len(list) == 0 :
        print(-1)
    else :
        print(list[0])
       
    return list

def eight(list = lists):
    if len(list) == 0:
        print(-1)
    else :
        print(list[-1])

    return list
        
num = int(sys.stdin.readline())

for _ in range(num):
    commands = list(map(int, sys.stdin.readline().split()))
    
    if commands[0] == 1:
        lists = one(commands[1], lists)
    elif commands[0] == 2:
        lists = two(commands[1], lists)
    elif commands[0] == 3:
        lists = three(lists)
    elif commands[0] == 4:
        lists = four(lists)
    elif commands[0] == 5:
        lists = five(lists)
    elif commands[0] == 6:
        lists = six(lists)
    elif commands[0] == 7:
        lists = seven(lists)
    elif commands[0] == 8:
        lists = eight(lists)