from collections import deque

num = int(input())
a = int(input())

lists = [[] for i in range(num+1)]

for _ in range(a):
    b, c = map(int, input().split())
    lists[b].append(c)
    lists[c].append(b)
    
queue = deque([1])
visited = [False] * (num+1)
visited[1] = True

while queue:
    node = queue.popleft()
    for neighbor in lists[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
print(sum(visited) - 1)
        