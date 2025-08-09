def solution(triangle):
    dp = triangle[-1][:]

    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + max(dp[j], dp[j+1])
    return dp[0]