import sys
sys.setrecursionlimit(10000)


def dfs(m, n):
    global cnt
    x_move = [0,0,1,-1]
    y_move = [1,-1,0,0]
    
    for i in range(4):
        x = m + x_move[i]
        y = n + y_move[i]
        if (x >= 0 and x < num) and (y >= 0 and y < num) :
            if lists[x][y] == 1:
                cnt +=1
                lists[x][y] = 0
                dfs(x, y)

num = int(input())

lists = []
for _ in range(num):
    a = input().strip() 
    lists.append([int(i) for i in a])

answer = []
for m in range(num) : #가로
    for n in range(num) : #세로
        if lists[m][n] == 1:
            cnt = 1
            lists[m][n] = 0
            dfs(m,n)
            answer.append(cnt) 

answer.sort()
print(len(answer))
for i in answer:
    print(i)