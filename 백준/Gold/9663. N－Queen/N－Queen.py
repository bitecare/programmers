n = int(input())  # 체스판 크기 입력
cnt = 0  # 가능한 배치의 경우의 수

# 열, 대각선 상태를 추적할 배열
cols = [False] * n       # 각 열에 퀸이 배치되었는지 확인
diag1 = [False] * (2 * n - 1)  # 좌상-우하 대각선에 퀸이 배치되었는지 확인
diag2 = [False] * (2 * n - 1)  # 우상-좌하 대각선에 퀸이 배치되었는지 확인

def dfs(row):
    global cnt

    if row == n:  # 퀸을 모두 배치했다면
        cnt += 1  # 가능한 배치 카운트 증가
        return

    # 각 열에 대해 퀸을 배치
    for col in range(n):
        # 해당 열과 대각선에 퀸을 배치할 수 있는지 확인
        if not cols[col] and not diag1[row + col] and not diag2[row - col + (n - 1)]:
            # 퀸을 배치한 후, 상태를 업데이트
            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + (n - 1)] = True
            
            # 다음 행으로 이동
            dfs(row + 1)
            
            # 백트래킹: 퀸을 제거하고 상태를 되돌림
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + (n - 1)] = False

# DFS 호출
dfs(0)
print(cnt)  # 가능한 배치의 총 개수 출력
