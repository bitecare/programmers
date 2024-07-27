import sys

num = int(sys.stdin.readline())

def num_round(x):
    if x > 0:
        if x >= int(x) + 0.5:
            return int(x) + 1
        else:
            return int(x)
    else:
        if x <= int(x) - 0.5:
            return int(x) - 1
        else:
            return int(x)

lists = []
dic = {}
for i in range(num):
    a = int(sys.stdin.readline())
    lists.append(a)
    if lists[i] not in dic:
        dic[lists[i]] = 1
    else :
        dic[lists[i]] +=1
lists = sorted(lists)
print(num_round(sum(lists) / len(lists)))
print(lists[int(len(lists)/2)])

modes = sorted([[i,v] for i,v in dic.items() if v == max(dic.values())])
if len(modes) >= 2:
    print(modes[1][0])
else :
    print(modes[0][0])
print(max(lists) - min(lists))