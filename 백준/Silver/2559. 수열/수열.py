a, b = map(int, input().split())

lists = list(map(int, input().split()))
sums = sum(lists[:b])
ans = sums

for i in range(a-b):
    sums = sums - lists[i] + lists[i+b]
    if sums >= ans:
        ans = sums
print(ans)