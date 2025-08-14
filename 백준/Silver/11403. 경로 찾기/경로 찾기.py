import sys
from collections import deque

input = sys.stdin.readline
num = int(input())

lists = []
for _ in range(num):
    lists.append(list(map(int, input().split())))

maps = [[] for _ in range(num+1)]

for i in range(len(lists)):
    for j in range(len(lists)):
        if lists[i][j] == 1:
            maps[i+1].append(j+1)

def dfs(maps, start):
    visited = [False] * len(maps)
    queue = deque([start])
    #visited[start] = True

    while queue:
        q = queue.popleft()
        for i in maps[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return visited

for i in range(1, num+1):
    case = dfs(maps, i)
    print(*[1 if i == True else 0 for i in case[1:]])
