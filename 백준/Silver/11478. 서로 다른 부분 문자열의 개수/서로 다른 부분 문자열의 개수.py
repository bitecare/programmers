a = input()

lists = []

for i in range(len(a)):
    for j in range(i+len(a)+1):
        lists.append(a[i:i+j])
lists = set(lists)
lists.remove("")
print(len(lists))