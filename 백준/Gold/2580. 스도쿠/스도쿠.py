lists = []
zero_lists = []


for _ in range(9):
    lists.append(list(map(int, input().split())))


for i in range(9):
    for j in range(9):
        if lists[i][j] == 0:
            zero_lists.append([i, j])

target = len(zero_lists)


def is_valid(board, row, col, num):

    for c in range(9):
        if board[row][c] == num:
            return False
    
    for r in range(9):
        if board[r][col] == num:
            return False
    
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def dfs(depth, lists):
    global found  
    
    if depth == target:
        for i in range(9):
            print(*lists[i])  
        found = True  
        return  

    i, j = zero_lists[depth]
    for m in range(1, 10):
        if is_valid(lists, i, j, m):
            lists[i][j] = m  
            dfs(depth + 1, lists) 
            if found:  
                return
            lists[i][j] = 0 

found = False

dfs(0, lists)
