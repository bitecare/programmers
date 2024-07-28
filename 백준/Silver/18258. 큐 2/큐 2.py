import sys
from collections import deque

lists = deque()

def push(x, list = lists):
    list.append(x)
    return list
    
def pop(list = lists):
    if len(list) == 0:
        print("-1")
    else :
        b = list.popleft()
        print(b)
        
    return list
    
def size(list = lists):
    print(len(list))
    return list

def empty(list = lists):
    if len(list) == 0:
        print(1)
    else :
        print(0)
    
    return list

def front(list = lists):
    if len(list) == 0:
        print(-1)
    else :
        print(list[0])
    
    return list

def back(list = lists):
    if len(list) == 0:
        print(-1)
    else :
        print(list[-1])
    
    return list

num = int(sys.stdin.readline())

for _ in range(num):
    
    commands = sys.stdin.readline().split()
    
    if commands[0] == "push" :
        list = push(int(commands[1]))
    
    elif commands[0] == "pop":
        list = pop()
        
    elif commands[0] == "size":
        list = size()
    
    elif commands[0] == "empty":
        list = empty()
    
    elif commands[0] == "front":
        list = front()
        
    elif commands[0] == "back":
        list = back()
         