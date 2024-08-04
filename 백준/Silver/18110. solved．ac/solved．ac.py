import sys

num = int(sys.stdin.readline())

def num_round(x):
    if x >= int(x) + 0.5 :
        return int(x) + 1
    else :
        return int(x)

lists = []
for _ in range(num):
    a = int(sys.stdin.readline())
    lists.append(a)

if num >= 1:
    lists = sorted(lists)
    deletes = num_round(num * 0.15)
    lists = lists[deletes : len(lists) - deletes]
    b = (sum(lists) / len(lists))
    print(num_round(b))

else :
    print(0)