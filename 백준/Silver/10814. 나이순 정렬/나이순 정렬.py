num = int(input())

lists = []
for i in range(num):
    a = list(input().split())
    a.append(i)
    lists.append(a)
    
lists = sorted(lists, key = lambda x : [int(x[0]), int(x[2])])

for i in lists:
    print(i[0], i[1])