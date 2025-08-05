import sys
input = sys.stdin.readline

while True:
    num = int(input())
    if num == 0 :
        break
    lists = []
    dp = [0] * num

    for _ in range(num):
        profit = int(input())
        lists.append(profit)

    dp[0] = lists[0]

    for i in range(1, len(lists)):
        dp[i] = max(dp[i-1] + lists[i], lists[i])

    print(max(dp))
    