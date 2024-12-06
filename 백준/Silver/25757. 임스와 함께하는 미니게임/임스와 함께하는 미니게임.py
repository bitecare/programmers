a,b = input().split()
lists = []

for _ in range(int(a)):
    lists.append(input())

lists = list(set(lists))

if b == "Y":
    print(len(lists))
elif b == "F":
    print(len(lists) // 2)
else :
    print(len(lists) // 3)