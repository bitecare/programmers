a, b = map(int, input().split())

a_lists = set()
b_lists = []
add = 0
for _ in range(a):
    a_lists.add(input())

for _ in range(b):
    b_lists.append(input())

for i in range(len(b_lists)) :
    if b_lists[i] in a_lists:
        add +=1

print(add)
        