n = int(input())

lists = [0]*(n+1)
dp = [0]*(n+1)

for i in range(1, n+1):
    lists[i] = int(input())

if n == 1:
    print(lists[1])
    exit()

elif n == 2:
    print(sum(lists))
    exit()

dp[1] = lists[1]
dp[2] = lists[1] + lists[2]

for i in range(3, n+1):
    dp[i] = max((dp[i-2] + lists[i]), (dp[i-3] + lists[i-1] + lists[i]))

print(dp[-1])
        