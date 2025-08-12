from collections import deque

node, edge, start = map(int, input().split())
lists = []

for _ in range(edge):
    lists.append(list(map(int, input().split())))

graph = [[] for _ in range(node + 1)]

for m, n in lists:
    graph[m].append(n)
    graph[n].append(m)


def dfs(graph, start):
    
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end = " ")

            for i in sorted(graph[node], reverse=True):
                if not visited[i]:
                    stack.append(i)

def bfs(graph, start):

    visited = [False] * len(graph)
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if not visited[node] :
            visited[node] = True
            print(node, end = " ")

            for i in sorted(graph[node]):
                if not visited[i]:
                    queue.append(i)

dfs(graph, start)
print()
bfs(graph, start)
