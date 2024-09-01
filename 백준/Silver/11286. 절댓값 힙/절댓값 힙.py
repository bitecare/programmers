import heapq
import sys

num = int(sys.stdin.readline())
heap = []

for _ in range(num):
    num2 = int(sys.stdin.readline())

    if num2 == 0:
        if not heap: 
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num2), num2))