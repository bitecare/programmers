words = list(input())
bomb = list(input())
lists = []

for i in words:
    lists.append(i)
    if lists[-len(bomb):] == bomb :
        for _ in range(len(bomb)):
            lists.pop()
if len(lists) == 0:
    print("FRULA")
else :
    print(''.join(lists))
