import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

lists = []

for _ in range(m):
    lists.append(list(map(int, input().split())))

maps = [[] for _ in range(n + 1)]

for i,j in lists:
    maps[i].append(j)
    maps[j].append(i)

def bfs(maps, start, end):

    dist = [0] * len(maps)
    queue = deque([start])
    
    while queue:
        q = queue.popleft()
        if q == end:
            break
        for i in maps[q]:
            if dist[i] == 0:
                dist[i] = dist[q] + 1
                queue.append(i)
    return dist[end]

answer = []

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        cnt += bfs(maps, i, j)
    answer.append(cnt)

print(answer.index(min(answer))+1)