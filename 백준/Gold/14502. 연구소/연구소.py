import copy

n, m = map(int, input().split())
maps = []
max_safe_area = -1e9

for _ in range(n):
    maps.append(list(map(int, input().split())))

def virus_spread(map, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
                map[nx][ny] = 2
                queue.append((nx,ny))
                
def calculate():

    temp_map = copy.deepcopy(maps)

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                virus_spread(temp_map, i ,j)

    safe_area = 0
    for i in range(n):
        safe_area += temp_map[i].count(0)
    return safe_area
 
def backtrack(depth, idx):
    global max_safe_area
    
    if depth == 3:
        result = calculate()
        max_safe_area = max(result, max_safe_area)
        return 
        
    for k in range(idx, n * m):
        i = k // m
        j = k % m

        if maps[i][j] == 0 :
            maps[i][j] = 1
            backtrack(depth + 1, k + 1)
            maps[i][j] = 0

backtrack(0,0)

print(max_safe_area)