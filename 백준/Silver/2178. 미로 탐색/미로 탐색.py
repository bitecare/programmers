from collections import deque

n, m = map(int, input().split())

lists = []
for _ in range(n):
    a = input()
    lists.append(list(map(int, str(a))))

def bfs(maze, n, m):
    queue = deque([(0,0)])
    maze[0][0] = 2
    
    while queue:
        x, y = queue.popleft()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1] - 1

answer = bfs(lists, n, m)
print(answer)