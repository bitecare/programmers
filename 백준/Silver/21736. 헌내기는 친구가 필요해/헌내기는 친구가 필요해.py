import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

lists = []

for _ in range(m):
    lists.append(list(input()))

#도연이 위치 찾기
for i in range(m):
    for j in range(n):
        if lists[i][j] == "I" :
            start_x = j
            start_y = i
            break

#길 찾기
def bfs(board, start_x, start_y):
    q = deque([(start_y, start_x)])
    visited = [[False] * n for _ in range(m)]
    visited[start_y][start_x] = True
    cnt = 0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= ny < m and 0 <= nx < n) :
                continue
            if visited[ny][nx] or board[ny][nx] == "X" :
                continue
            visited[ny][nx] = True
            if board[ny][nx] == "P":
                cnt +=1
            q.append((ny, nx))

    return cnt

cnt = bfs(lists, start_x, start_y)

if cnt == 0:
    print("TT")
else:
    print(cnt)