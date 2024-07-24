import sys

num = int(sys.stdin.readline())

lists = []
for _ in range(num):
    lists.append(int(sys.stdin.readline()))

lists = sorted(lists)

for j in lists:
    print(j)
