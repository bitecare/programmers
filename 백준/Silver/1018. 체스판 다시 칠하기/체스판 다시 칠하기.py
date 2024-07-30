row, col = map(int, input().split())

board = []
for _ in range(row):
    a = list(input())
    board.append(a)

tile_num = []
for i in range(row - 8 + 1):
    for j in range(col - 8 + 1):
        count1 = 0
        count2 = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:
                    if board[i + k][j + l] != 'B':
                        count1 += 1
                    if board[i + k][j + l] != 'W':
                        count2 += 1
                else:
                    if board[i + k][j + l] != 'W':
                        count1 += 1
                    if board[i + k][j + l] != 'B':
                        count2 += 1
        tile_num.append(min(count1, count2))

print(min(tile_num))
