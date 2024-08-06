num = int(input())

lists = sorted(list(map(int, input().split())))
ans = 0

for i in range(len(lists)):
    ans = ans + lists[i] * (len(lists)-i)

print(ans)
