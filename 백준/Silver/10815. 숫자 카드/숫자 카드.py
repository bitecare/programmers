import sys

input = sys.stdin.readline

a = int(input())

lists = set(list(map(int, input().split())))

b = int(input())

b_list = list(map(int, input().split()))

for i in range(len(b_list)) :
    if b_list[i] in lists:
        b_list[i] = 1
    else :
        b_list[i] = 0

print(*b_list)
    