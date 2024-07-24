num = int(input())

lists = []
for _ in range(num):
    a = list(map(int, input().split()))
    lists.append(a)

lists = sorted(lists)

for i in lists:
    print(*i)