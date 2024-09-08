import sys

a, b = map(int, sys.stdin.readline().split())

dic_lists = {}
for _ in range(a):
    words = sys.stdin.readline().rstrip()

    if len(words) >= b :

        if words in dic_lists:
            dic_lists[words] +=1
        else :
            dic_lists[words] = 1

dic_lists = sorted(dic_lists.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(dic_lists)):
    print(dic_lists[i][0])