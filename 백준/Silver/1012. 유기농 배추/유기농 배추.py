import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < m) and (0 <= ny < n):
            if lists[ny][nx] == 1:
                lists[ny][nx] = 0
                dfs(nx, ny)

num = int(sys.stdin.readline())
for _ in range(num):
    ans = 0
    m, n, k = map(int, sys.stdin.readline().split()) #m이 가로 n이 세로
    lists = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split()) #a가 가로 b가 세로
        lists[b][a] = 1

    for i in range(m):
        for j in range(n):
            if lists[j][i] == 1:
                dfs(i,j)
                ans +=1
    print(ans)