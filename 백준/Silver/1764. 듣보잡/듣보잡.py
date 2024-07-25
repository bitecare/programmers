a, b = map(int, input().split())

group_a = []
group_b = []
for i in range(a+b):
    if i <= (a-1) :
        group_a.append(input())
    else :
        group_b.append(input())

inter = (set(group_a) & set(group_b))
print(len(inter))
inter = sorted(list(inter))
for i in inter:
    print(i)
    