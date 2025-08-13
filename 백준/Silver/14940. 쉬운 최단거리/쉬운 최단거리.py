import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

start_x = 0
start_y = 0
lists = []

for _ in range(n):
    lists.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if lists[i][j] == 2:
            start_x = j
            start_y = i
            break

def bfs(board, start_y, start_x):
    len_x = len(board[0])
    len_y = len(board)
    
    answer = [[-1] * len_x for _ in range(len_y)]
    answer[start_y][start_x] = 0
    queue = deque([(start_y, start_x)])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        sy, sx = queue.popleft()
        for i in range(4):
            x = sx + dx[i]
            y = sy + dy[i]

            if (0 <= y < len_y and 0 <= x < len_x):
                if board[y][x] != 0 and answer[y][x] == -1  :
                    answer[y][x] = answer[sy][sx] + 1
                    queue.append((y,x))
                    
    return answer

answer = bfs(lists, start_y, start_x)

for i in range(n):
    for j in range(m):
        if lists[i][j] == 0 and answer[i][j] == -1 :
            answer[i][j] = 0
    print(*answer[i])
