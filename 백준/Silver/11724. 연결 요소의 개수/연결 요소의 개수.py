import sys
input = sys.stdin.readline
node, edge = map(int, input().split())

lists = []
for _ in range(edge):
    lists.append(list(map(int, input().split())))

graph = [[] for _ in range(node + 1)]

for m, n in lists:
    graph[m].append(n)
    graph[n].append(m)

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

def count_graph(graph):
    visited = [False] * len(graph)
    count = 0

    for i in range(1, len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            count +=1

    return count

print(count_graph(graph))