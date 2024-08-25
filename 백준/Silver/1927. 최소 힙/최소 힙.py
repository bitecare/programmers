import heapq
import sys

num = int(sys.stdin.readline())
lists = []

for _ in range(num):
    a = int(sys.stdin.readline())
    
    if a == 0 :
        if len(lists) == 0 :
            print(0)
        else :
            print(heapq.heappop(lists))
    else :
        heapq.heappush(lists, a)