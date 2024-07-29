num = int(input())

lists = list(map(int, input().split()))

print(max(lists) * min(lists))