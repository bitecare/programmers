num = int(input())

lists = []

for _ in range(num):
    a, b = input().split()
    if a == "ChongChong" or b == "ChongChong" :
        lists.append(a)
        lists.append(b)
    else :
        if a in lists:
            lists.append(b)
        elif b in lists:
            lists.append(a)
print(len(set(lists)))